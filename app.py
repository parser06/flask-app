from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from pymongo import MongoClient
import os
import uuid

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://charity_user:your_password_here@cluster0.8swpuom.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # replace if not using env
client = MongoClient(MONGO_URI)
db = client['charity_db']
charity_collection = db['charities']

# Serve index.html when visiting the root
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')


# Get data from MongoDB
@app.route('/api/charities')
def get_charities():
    charities = list(charity_collection.find({}, {'_id': 0}))  # exclude MongoDB's _id field
    return jsonify(charities)

'''
# Serve the charities API
@app.route('/api/charities')
def get_charities():
    return jsonify([
        {"name": "UNICEF", "url": "https://www.unicef.org"},
        {"name": "Red Cross", "url": "https://www.redcross.org"},
        {"name": "Charity: Water", "url": "https://www.charitywater.org"},
        {"name": "Doctors Without Borders", "url": "https://www.doctorswithoutborders.org/"},
    ])
'''

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