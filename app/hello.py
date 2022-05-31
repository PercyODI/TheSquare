from flask import Flask

app = Flask(__name__,
            static_folder="client",
            static_url_path="/app")


@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"
