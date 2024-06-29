# JSON Config Editor

## Features

- Edit any JSON configuration file through a web interface
- Supports nested objects, arrays, and various data types
- Basic authentication for security
- Easy integration into existing Flask applications

A web-based JSON configuration editor with authentication.

## Example 

![JSON Config Editor Screenshot](examples/screenshot.png)

## Usage

```python
from json_ui import create_app

if __name__ == '__main__':
    app = create_app(
        config_path='/path/to/your/config.json',
        username='admin',
        password='your_secure_password'
    )
    app.run(host='0.0.0.0', port=5000)
```
