from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello from Flask!"

@app.route("/test", methods=["POST"])
def test():
    data = request.json
    time.sleep(1)
    return jsonify({
        "status": "success",
        "user_id": data.get("user_id")
    })
