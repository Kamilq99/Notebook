from flask import Blueprint, jsonify
from model.note import Note

show_notes_bp = Blueprint('show_notes', __name__)

@show_notes_bp.route('/api/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()

    # przygotowanie czystego JSONa
    result = []
    for note in notes:
        result.append({
            "id": note.id,
            "title": note.title,
            "author": note.author,
            "content": note.content,
            # jeśli masz daty:
            # "created_at": note.created_at.isoformat() if note.created_at else None
        })

    return jsonify(result), 200
