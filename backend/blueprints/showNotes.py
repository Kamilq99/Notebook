from flask import Blueprint, jsonify, current_app

show_notes_bp = Blueprint('show_notes', __name__)

@show_notes_bp.route('/api/notes', methods=['GET'])
def show_notes():
    es = current_app.config['ES']
    index_name = current_app.config['NOTES_INDEX']

    try:
        res = es.search(
            index=index_name,
            query={"match_all": {}}
        )

        notes = [
            {
                "id": hit["_id"],
                "title": hit["_source"].get("title"),
                "author": hit["_source"].get("author"),
                "content": hit["_source"].get("content"),
            }
            for hit in res["hits"]["hits"]
        ]

        return jsonify(notes), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
