from flask import Blueprint, jsonify, current_app
from elasticsearch import NotFoundError

delete_note_bp = Blueprint('delete_note', __name__)

@delete_note_bp.route('/api/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    es = current_app.config['ES']
    index_name = current_app.config['NOTES_INDEX']

    try:
        es.delete(index=index_name, id=note_id)
        return jsonify({"message": "Note deleted"}), 200

    except NotFoundError:
        return jsonify({"error": "Note not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500
