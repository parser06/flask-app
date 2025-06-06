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
