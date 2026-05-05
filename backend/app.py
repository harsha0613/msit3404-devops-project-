from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Flask Backend</title>
  <style>
    body { font-family: Segoe UI, sans-serif; text-align: center; padding: 60px; background: #f7fafc; }
    h1 { color: #2d3748; }
    img { margin-top: 24px; max-width: 560px; width: 100%; border-radius: 10px; box-shadow: 0 4px 16px rgba(0,0,0,0.1); }
  </style>
</head>
<body>
  <h1>Hello from Flask Backend!</h1>
  <img src="/static/image.jpg" alt="Static Image" />
</body>
</html>'''


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
