from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Your Problem</h1>"


@app.route("/shop")
def about():
    return "<h1>Marketplace</h1>"


if __name__ == '__main__':
    app.run(debug=True)
