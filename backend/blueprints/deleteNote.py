from flask import Blueprint, request, jsonify
from model.note import Note

delete_note_bp = Blueprint('delete_note', __name__)

def init_routes(es, index_name='notes'):
    @delete_note_bp.route('/api/notes/<note_id>', methods=['DELETE'])
    def delete_note(note_id):
        # Delete note from Elasticsearch
        res = es.delete(index=index_name, id=note_id)
        
        return jsonify({"message": "Note deleted", "id": res['_id']}), 200