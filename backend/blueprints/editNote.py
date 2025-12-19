from flask import Blueprint, request, jsonify, current_app
from elasticsearch import NotFoundError

edit_note_bp = Blueprint('edit_note', __name__)

@edit_note_bp.route('/api/notes/<note_id>', methods=['PUT'])
def edit_note(note_id):
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

    doc = {
        "title": title,
        "author": author,
        "content": content
    }

    try:
        # 🔹 dodajemy refresh=True, aby zmiany były widoczne od razu
        res = es.update(
            index=index_name,
            id=note_id,
            doc={"doc": doc},
            refresh=True
        )

        return jsonify({
            "message": "Note updated",
            "id": res["_id"]
        }), 200

    except NotFoundError:
        return jsonify({"error": "Note not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500
