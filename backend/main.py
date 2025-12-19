from flask import Flask
from blueprints import (
    add_note_bp,
    delete_note_bp,
    edit_note_bp,
    show_notes_bp
)
from config import init_app_config

app = Flask(__name__)

init_app_config(app)

app.register_blueprint(add_note_bp)
app.register_blueprint(delete_note_bp)
app.register_blueprint(edit_note_bp)
app.register_blueprint(show_notes_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
