from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    print("NEW RESPONSE:", data)

    with open("responses.txt", "a") as f:
        f.write(json.dumps(data) + "\n")

    return {"status": "received"}

@app.route("/")
def home():
    return "Server running"

@app.route("/responses")
def responses():
    with open("responses.txt", "r") as f:
        return f.read()

app.run(host="0.0.0.0", port=10000)

