from flask import Flask, render_template, url_for
import itemAPI
app = Flask(__name__)


@app.route("/")
def input():
    return render_template('input.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/shop")
def about():
    return render_template('shop.html', items=itemAPI.createItemDictFromCSV())


if __name__ == '__main__':
    app.run(debug=True)
