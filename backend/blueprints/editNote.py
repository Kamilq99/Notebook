from flask import Blueprint, request, jsonify
from model.note import Note

edit_note_bp = Blueprint('edit_note', __name__)

@edit_note_bp.route('/api/editNote/<int:note_id>', methods=['PUT'])
def edit_note(note_id):
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    content = data.get('content')

    if not title or not author or not content:
        return jsonify({'error': 'Missing required fields'}), 400

    # Here you would typically fetch the note from your database
    # For example: note = Note.query.get(note_id)
    # Then update its fields and save it back to the database
    # note.title = title
    # note.author = author
    # note.content = content
    # db.session.commit()

    return jsonify({'message': f'Note with id {note_id} updated successfully', 
                    'note': {'id': note_id, 'title': title, 'author': author, 'content': content}}), 200