from flask import Flask, request
from flask import json
import logging

app = Flask(__name__)
logging.basicConfig(
        filename="app.log",
        level=logging.DEBUG,
        format="%(asctime)s, %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )

def log():
    app.logger.info(f"{request.path} endpoint was reached")

@app.route("/status")
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json",
    )
    log()
    return response


@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps(
            {
                "status": "success",
                "code": 0,
                "data": {"UserCount": 140, "UserCountActive": 23},
            }
        ),
        status=200,
        mimetype="application/json",
    )
    log()
    return response


@app.route("/")
def hello():
    log()
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
