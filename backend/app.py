from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to AWS 3-Tier Infrastructure Project"
    })

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "AWS 3-Tier Backend"
    })

@app.route("/api/message")
def message():
    return jsonify({
        "message": "Backend is successfully connected!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
