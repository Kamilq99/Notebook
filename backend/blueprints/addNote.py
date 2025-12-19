from flask import Blueprint, request, jsonify
from model.note import Note

add_note_bp = Blueprint('add_note', __name__)

def init_routes(es, index_name = 'notes'):
    @add_note_bp.route('/api/notes', methods=['POST'])
    def add_note():
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        content = data.get('content')

        if not title or not author or not content:
            return jsonify({"error": "Title, author, and content are required"}), 400

        note = Note(title=title, author=author, content=content)

        # Insert note into Elasticsearch
        doc = {
            'title': note.title,
            'author': note.author,
            'content': note.content
        }
        res = es.index(index=index_name, document=doc)
        
        return jsonify({"message": "Note added", "id": res['_id']}), 201