from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Serve index.html when visiting the root
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve the charities API
@app.route('/api/charities')
def get_charities():
    return jsonify([
        {"name": "UNICEF", "url": "https://www.unicef.org"},
        {"name": "Red Cross", "url": "https://www.redcross.org"},
        {"name": "Charity: Water", "url": "https://www.charitywater.org"},
    ])

# Optional: Serve other static files (CSS, JS)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


'''
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello from Flask on Render!"

@app.route('/api/charities')
def charities():
    return jsonify([
        {"name": "UNICEF", "url": "https://www.unicef.org"},
        {"name": "Red Cross", "url": "https://www.redcross.org"},
        {"name": "Charity: Water", "url": "https://www.charitywater.org"},
    ])

if __name__ == '__main__':
    app.run()
'''
