import flask

app = flask.Flask(__name__)

port = 80

local_ip = "0.0.0.0"


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host=local_ip, port=port)
