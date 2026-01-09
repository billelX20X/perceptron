
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


import time

@app.route("/test", methods=["POST"])
def test():
    data = request.json

    time.sleep(1)

    return jsonify({
        "status": "success",
        "user_id": data.get("user_id")
    })

if __name__ =="__main__":
    app.run()



