from flask import Blueprint, request, jsonify
from model.note import Note

delete_note_bp = Blueprint('delete_note', __name__)
@delete_note_bp.route('/api/deleteNote/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    # Here you would typically delete the note from your database
    # For example: note = Note.query.get(note_id); db.session.delete(note); db.session.commit()
    return jsonify({'message': f'Note with id {note_id} deleted successfully'}), 200