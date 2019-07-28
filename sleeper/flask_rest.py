from flask_restful import Api
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS

import uuid
import os
import subprocess

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route("/look_busy")
def look_busy():
    n = request.args.get("n", default=None, type=int)

    os.sleep(n)

    return jsonify({
        "n": n,
        "response_id": uuid.uuid4()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="1234")
