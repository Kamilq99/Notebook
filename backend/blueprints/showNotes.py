from flask import Blueprint, jsonify
from model.note import Note

show_notes_bp = Blueprint('show_notes', __name__)

def init_routes(es, index_name='notes'):
    @show_notes_bp.route('/api/notes', methods=['GET'])
    def show_notes():
        # Fetch all notes from Elasticsearch
        res = es.search(index=index_name, body={"query": {"match_all": {}}})
        notes = []
        for hit in res['hits']['hits']:
            source = hit['_source']
            note = Note(
                title=source['title'],
                author=source['author'],
                content=source['content']
            )
            notes.append({
                'id': hit['_id'],
                'title': note.title,
                'author': note.author,
                'content': note.content
            })
        
        return jsonify(notes), 200
