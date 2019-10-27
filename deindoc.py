from flask import Flask, render_template, url_for, flash, redirect, request
import itemAPI
from forms import ButtonForm
import json
import requests
import http.client
import pickle
app = Flask(__name__)

model = pickle.load(open('model.sav', 'rb'))

cartList = []

api_token = "gAAAAMA_MWOas38X6QqzABin1xvPd5RiCaDTYTzbjcJlGVhDO8zfEFAIs_F4OM_KTPhhhg75uZYLEXEys3BtdzGCU5awJLEx6y86yEQ4DbuHc0eygkQqNe_IVzRLB2y_kz72eaYNg5Gmb1Nyo6XCcTtNTu7o9oWAdMY9TFP490lRtati9AAAAIAAAABLQmFuEkaDIEHkuosYILnK5nV1XE647K1h7cvzx5Fai7R3rsWAImg-PKoW8Sahyj2nge7DDEhC0FFs8BC8NJFNgtiAEowuECD6ZJ88ze66ma-qpe2RgBdey8WdVjl7LTY-JYoEGhPyT21yzUpFgl_1r8QXKd7UgA_vXosFJC2vMBb_bgrtScAiVLD8oL6MPFAFyTkVR7H4Dk_s3zCsO6gTQlmT8cIjn86kW6t-p8ANySY7uFAsHNqib5qHz-_SHxVlhiusFZdl0bjQxNk3y-sEmpqTe7rxzke7fzenADutQKuqr2ONexylvlUvLhbY0"
client_id = "gt_552463"
client_secret = "004e007a-004a-0035-4b00-740033006800"

headers = {'Authorization': 'Bearer {0}'.format(api_token), 'Accept': 'application/json'}


conn = http.client.HTTPSConnection("api-reg.ncrsilverlab.com")

payload = "{\"Orders\": [{\"IsClosed\":true,\"OrderNumber\":\"string\",\"OrderDateTime\":\"2019-10-27T00:38:56.555Z\",\"OrderDueDateTime\":\"2019-10-27T00:38:56.555Z\",\"IsPaid\":true,\"Customer\":{\"CustomerId\":0,\"CustomerName\":\"string\",\"Email\":\"string\",\"PhoneNumber\":\"string\",\"Address1\":\"string\",\"Address2\":\"string\",\"Address3\":\"string\",\"City\":\"string\",\"State\":\"string\",\"ZipCode\":\"string\"},\"CustomerId\":0,\"CustomerName\":\"string\",\"Email\":\"string\",\"PhoneNumber\":\"string\",\"TableReference\":\"string\",\"TaxAmount\": 0,\"TipAmount\": 0,\"LineItems\":[{\"ExternalItemId\":\"1710184\",\"ItemName\":\"string\",\"Quantity\":1,\"UnitPrice\":0,\"UnitSellPrice\":0,\"ExtendedSellPrice\":0,\"Notes\":[\"string\"],\"BagName\":\"string\"}],\"Notes\":[\"string\"],\"KitchenLeadTimeInMinutes\":0,\"SkipReceipt\":true,\"SkipKitchen\":true,]}],\"SourceApplicationName\":\"string\"}"

conn.request("POST", "/orders", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


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
    return render_template('shop.html', items=itemAPI.createItemDictFromCSV(), form=form, model=model)

@app.route("/addToCart")
def addToCart():
	item_id = request.args.get('item_id')
	cartList.append(int(item_id))
	print(cartList)

	return about()

@app.route("/cart")
def cart():
	return render_template('cart.html', items = itemAPI.createIDDictFromCSV(),cartList = cartList)
if __name__ == '__main__':
    app.run(debug=True)


def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
