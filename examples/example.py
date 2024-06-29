from pathlib import Path
from json_ui import create_app

if __name__ == '__main__':
    app = create_app(
        config_path=Path(__file__).parent / 'config.json',
        username='admin',
        password='password'
    )
    app.run(host='0.0.0.0', port=5000)
