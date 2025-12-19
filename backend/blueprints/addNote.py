from flask import Blueprint, request, jsonify, current_app
from model.note import Note

add_note_bp = Blueprint('add_note', __name__)

@add_note_bp.route('/api/notes', methods=['POST'])
def add_note():
    es = current_app.config['ES']
    index_name = current_app.config['NOTES_INDEX']

    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON body"}), 400

    title = data.get('title')
    author = data.get('author')
    content = data.get('content')

    if not title or not author or not content:
        return jsonify({"error": "Title, author, and content are required"}), 400

    note = Note(title=title, author=author, content=content)

    res = es.index(
        index=index_name,
        document=note.__dict__
    )

    return jsonify({
        "message": "Note added",
        "id": res["_id"]
    }), 201
