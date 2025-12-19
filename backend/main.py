from flask import Flask
from blueprints import (
    add_note_bp,
    delete_note_bp,
    edit_note_bp,
    show_notes_bp
)

app = Flask(__name__)

app.register_blueprint(add_note_bp)
app.register_blueprint(delete_note_bp)
app.register_blueprint(edit_note_bp)
app.register_blueprint(show_notes_bp)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)