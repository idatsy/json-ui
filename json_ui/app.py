from flask import Flask, render_template, request, jsonify
import json
from pathlib import Path
from .auth import auth, init_auth


def create_app(config_path, username, password):
    app = Flask(__name__)
    init_auth(username, password)

    config_file = Path(config_path)

    def load_config():
        with open(config_file, 'r') as f:
            return json.load(f)

    def save_config(config):
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=4)

    @app.route('/')
    @auth.login_required
    def index():
        config = load_config()
        return render_template('index.html', config=json.dumps(config))

    @app.route('/update_config', methods=['POST'])
    @auth.login_required
    def update_config():
        data = request.json
        save_config(data['config'])
        return jsonify({"status": "success"})

    return app
