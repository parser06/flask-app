from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
from flask import request
import uuid

app = Flask(__name__, static_folder='frontend', static_url_path='')
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
        {"name": "Doctors Without Borders", "url": "https://www.doctorswithoutborders.org/"},
    ])

@app.route('/api/donate', methods=['POST'])
def donate():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    amount = data.get("amount")
    charity = data.get("charityName")
    url = data.get("charityURL")

    # In a real app: send email, store in DB, etc.
    receipt_id = str(uuid.uuid4())

    print(f"[DONATION] {name} donated ${amount} to {charity} ({url})")

    return jsonify({"receiptId": receipt_id})

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
