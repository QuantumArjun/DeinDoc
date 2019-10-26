from flask import Flask, render_template, url_for, flash, redirect
import itemAPI
from forms import ButtonForm
app = Flask(__name__)


cart = {}

app.config['SECRET_KEY'] = 'dave'

@app.route("/")
def input():
    return render_template('input.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/shop")
def about():
    form = ButtonForm()
    return render_template('shop.html', items=itemAPI.createItemDictFromCSV(), form=form)

@app.route("/cart")
def cart():
	return render_template('cart.html', cart = itemAPI.createItemDictFromCSV())

if __name__ == '__main__':
    app.run(debug=True)
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)