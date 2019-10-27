from flask import Flask, render_template, url_for, flash, redirect, request
import itemAPI
import docAPI
from forms import ButtonForm
import json
import requests
import http.client
app = Flask(__name__)

cartList = []


url = "https://api-reg-apigee.ncrsilverlab.com/v2/orders"

querystring = {"store_number":"1"}

payload = "{\n    \n  \"Orders\": [\n    {\n      \"IsClosed\": true,\n      \"OrderNumber\": \"string\",\n      \"OrderDateTime\": \"2019-10-27T00:38:56.555Z\",\n      \"OrderDueDateTime\": \"2019-10-27T00:38:56.555Z\",\n      \"IsPaid\": true,\n      \"Customer\": {\n        \"CustomerId\": 0,\n        \"CustomerName\": \"string\",\n        \"Email\": \"string\",\n        \"PhoneNumber\": \"string\",\n        \"Address1\": \"string\",\n        \"Address2\": \"string\",\n        \"Address3\": \"string\",\n        \"City\": \"string\",\n        \"State\": \"string\",\n        \"ZipCode\": \"string\"\n      },\n      \"CustomerId\": 0,\n      \"CustomerName\": \"string\",\n      \"Email\": \"string\",\n      \"PhoneNumber\": \"string\",\n      \"TableReference\": \"string\",\n      \"TaxAmount\": 0,\n      \"TipAmount\": 0,\n      \"LineItems\": [\n        {\n          \"ExternalItemId\": \"2\",\n        \n          \"ItemName\": \"Ibuprofen\",\n          \"Quantity\": 1,\n          \"UnitPrice\": 2.99,\n          \"UnitSellPrice\": 2.99,\n          \"ExtendedSellPrice\": 2.99,\n          \n          \"Notes\": [\n            \"string\"\n          ],\n          \"BagName\": \"string\"\n        }\n      ],\n      \"Notes\": [\n        \"string\"\n      ],\n      \"KitchenLeadTimeInMinutes\": 0,\n      \"SkipReceipt\": true,\n      \"SkipKitchen\": true\n    }\n  ],\n  \"SourceApplicationName\": \"string\"\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Host': "api-reg-apigee.ncrsilverlab.com",
    'Authorization': "Bearer gAAAAK9vGlUfOoq9KZQ9YE-8RNoF-8f_ekV16a2w-_Fg7AGWcwe1H3fiqKQupZd4CLy4lUWKdqqG4K031kdGr1fqWcZzauSrWlg6H2kcO9x8YQpg4nmMgjQuBT9r1ErIy5h7rJ4UR7ImhDtHFc3IdCvvYkdsv_NFUhXNazMVCCENcJ0-9AAAAIAAAAA01H7Ogd1wa1gTr2RJ8ZmapL2jTSGeaPD9p_eS_9BTqExKvbq1OLWSrNjKL5dVyUGY7pJvEuw_ITcd9jNEQjnTfiVTCenoN1wTs1cLpgQxgAV2uXgDy12hqJ3BHW9erT3RCTX-z1IFPBchf6gNv0ZsDCP2tSJt4Brjyl7QzDWjoFvUkJJLwVdcwStWUJtjFcQ3QOS1UYuU7LDsHEo4t6pRZSO8STmFN0zjm0U42MYXbs4ocQD31m6n-aCeTjdVCNQ5ad7RwOJD9_O3oyyUf4FNNzIWis3GiszZI-paI-TsuF5wKBnxxVrWKyTOGQ5xGAY",
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

@app.route("/doc")
def doc():
    return render_template('doc.html', items=docAPI.createDocDictFromCSV())

	
if __name__ == '__main__':
    app.run(debug=True)




def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
