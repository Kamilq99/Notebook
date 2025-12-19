from flask import Blueprint, request, jsonify
from model.note import Note

add_note_bp = Blueprint('add_note', __name__)

@add_note_bp.route('/api/addNote', methods=['POST'])
def add_note():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    content = data.get('content')

    if not title or not author or not content:
        return jsonify({'error': 'Missing required fields'}), 400

    new_note = Note(title=title, author=author, content=content)
    # Here you would typically add the new_note to your database
    # For example: db.session.add(new_note); db.session.commit()

    return jsonify({'message': 'Note added successfully', 'note': new_note.__dict__}), 201