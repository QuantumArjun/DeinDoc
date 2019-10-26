from flask import Flask, render_template, url_for
import itemAPI
from forms import ButtonForm
app = Flask(__name__)


cart = {}

app.config['SECRET_KEY'] = ''

@app.route("/")
def input():
    return render_template('input.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/shop")
def about():
	
    return render_template('shop.html', items=itemAPI.createItemDictFromCSV())

@app.route("/cart")
def cart():
	return render_template('cart.html', cart = cart)

if __name__ == '__main__':
    app.run(debug=True)
