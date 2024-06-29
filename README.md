# JSON Editor

A web-based JSON editor with authentication.

## Installation

```bash
pip install json-config-editor
```

## Usage

```python
from json_config_editor import create_app

if __name__ == '__main__':
    app = create_app(
        config_path='/path/to/your/config.json',
        username='admin',
        password='your_secure_password'
    )
    app.run(host='0.0.0.0', port=5000)
```

## Features

- Edit any JSON file through a web interface
- Supports nested objects, arrays, and various data types
- Basic authentication for security
- Easy integration into existing Flask applications