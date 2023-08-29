from flask import Flask

app = Flask(__name__)

@app.route("/about", methods=["GET"])
def hello_world():
    return "<p>Novo Hello, World!</p>"


if "__main__" == __name__:
    app.run(debug=True)