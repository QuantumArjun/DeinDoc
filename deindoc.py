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


url = "https://api-reg-apigee.ncrsilverlab.com/v2/orders"

querystring = {"store_number":"1"}

payload = "{\n    \n  \"Orders\": [\n    {\n      \"IsClosed\": true,\n      \"OrderNumber\": \"string\",\n      \"OrderDateTime\": \"2019-10-27T00:38:56.555Z\",\n      \"OrderDueDateTime\": \"2019-10-27T00:38:56.555Z\",\n      \"IsPaid\": true,\n      \"Customer\": {\n        \"CustomerId\": 0,\n        \"CustomerName\": \"string\",\n        \"Email\": \"string\",\n        \"PhoneNumber\": \"string\",\n        \"Address1\": \"string\",\n        \"Address2\": \"string\",\n        \"Address3\": \"string\",\n        \"City\": \"string\",\n        \"State\": \"string\",\n        \"ZipCode\": \"string\"\n      },\n      \"CustomerId\": 0,\n      \"CustomerName\": \"string\",\n      \"Email\": \"string\",\n      \"PhoneNumber\": \"string\",\n      \"TableReference\": \"string\",\n      \"TaxAmount\": 0,\n      \"TipAmount\": 0,\n      \"LineItems\": [\n        {\n          \"ExternalItemId\": \"1710184\",\n        \n          \"ItemName\": \"string\",\n          \"Quantity\": 1,\n          \"UnitPrice\": 0,\n          \"UnitSellPrice\": 0,\n          \"ExtendedSellPrice\": 0,\n          \n          \"Notes\": [\n            \"string\"\n          ],\n          \"BagName\": \"string\"\n        }\n      ],\n      \"Notes\": [\n        \"string\"\n      ],\n      \"KitchenLeadTimeInMinutes\": 0,\n      \"SkipReceipt\": true,\n      \"SkipKitchen\": true\n    }\n  ],\n  \"SourceApplicationName\": \"string\"\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Host': "api-reg-apigee.ncrsilverlab.com",
    'Authorization': "Bearer gAAAAMA_MWOas38X6QqzABin1xvPd5RiCaDTYTzbjcJlGVhDO8zfEFAIs_F4OM_KTPhhhg75uZYLEXEys3BtdzGCU5awJLEx6y86yEQ4DbuHc0eygkQqNe_IVzRLB2y_kz72eaYNg5Gmb1Nyo6XCcTtNTu7o9oWAdMY9TFP490lRtati9AAAAIAAAABLQmFuEkaDIEHkuosYILnK5nV1XE647K1h7cvzx5F_ai7R3rsWAImg-PKoW8Sahyj2nge7DDEhC0FFs8BC8NJFNgtiAEowuECD6ZJ88ze66ma_-qpe2RgBdey8WdVjl7LTY-JYoEGhPyT21yzUpFgl_1r8QXKd7UgA_vXosFJC2vMBb_bgrtScAiVLD8oL6MPFAFyTkVR7H4Dk_s3zCsO6gTQlmT8cIjn86kW6t-p8ANySY7uFAsHNqib5qHz-_SHxVlhiusFZdl0bjQxNk3y-sEmpqTe7rxzke7fzenADutQKuqr2ONexylvlUvLhbY0",
    'cache-control': "no-cache",
    'Postman-Token': "40677c10-b4da-4d85-acf9-8791f890e36f"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)


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

@app.route("/doctors")
def doctors():
    return render_template('doc.html', items=docAPI.createDocDictFromCSV())


def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
