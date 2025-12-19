from flask import Blueprint, request, jsonify
from model.note import Note

edit_note_bp = Blueprint('edit_note', __name__)

def init_routes(es, index_name='notes'):
    @edit_note_bp.route('/api/notes/<note_id>', methods=['PUT'])
    def edit_note(note_id):
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        content = data.get('content')

        if not title or not author or not content:
            return jsonify({"error": "Title, author, and content are required"}), 400

        # Update note in Elasticsearch
        doc = {
            'title': title,
            'author': author,
            'content': content
        }
        res = es.update(index=index_name, id=note_id, doc={'doc': doc})
        
        return jsonify({"message": "Note updated", "id": res['_id']}), 200