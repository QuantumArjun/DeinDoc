from flask import Flask, render_template, url_for, flash, redirect, request
import itemAPI
import docAPI
from forms import ButtonForm
import json
import requests
import http.client
app = Flask(__name__)

cartList = []
currDisease = ['Asthma']
diseaseList = ['Asthma', 'Shingles', 'flu', 'Stomach Virus', 'Strep Throat']

url = "https://api-reg-apigee.ncrsilverlab.com/v2/orders"
token = "Bearer gAAAALOWxUkb73khqM2HJ9SJYjA3FQYHIaIRHfOdAeyg8u0q4M59-a2_scU1RYjlW96pW0U5fSPolx6bS9EICoM_2MUnJXqrQHgnyFcQfU1mzMjKTK3IJhSS_KYJ5u2_Nbn-H9n2nVpNzcVwEGF4eYdm-QR70_MNK1io1GKRUIxKlsIs9AAAAIAAAACdJDjvFGghIDFProy7AXjOXeJ0rolVhv2HUxnmhCpnkxQI_HDeFQdFDdubWQodjiW5ZDhPgyQw8paFx_6eS1vuEvAcyY7yvLJzsemZfIVgCUZ18yWTT1NMTIaxRBLO60DLidMB1Ria-JauVT-pn0GqkpYzabD5TZ1kjGN5Eacmj1Btem30rF4eTnsCjMuMgIYSpZ3kUJpfv28LlK1lgPERrWQaggRwBmL34MJJ7GvbPID4ui1v66S54vFa41oa4szJyb1wND2UJftzz9D0VB5-2rzc9STALRxlfenpvCDPrjPUxgBJNSdvgzAXPouj92o"
querystring = {"store_number":"1"}
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Host': "api-reg-apigee.ncrsilverlab.com",
    'Authorization': token,
    'cache-control': "no-cache",
    'Postman-Token': "40677c10-b4da-4d85-acf9-8791f890e36f"
    }
app.config['SECRET_KEY'] = 'dave'

def getAuth():
    url = "https://api-reg.ncrsilverlab.com/v2/OAuth2/token"

    headers = {
        'client_id': "gt_552463",
        'client_secret': "004e007a-004a-0035-4b00-740033006800",
        'cache-control': "no-cache",
        'Postman-Token': "96f96790-a161-407b-80e6-7cb4f773a37b"
        }

    authResponse = requests.request("GET", url, headers=headers)
    parsed_auth = (json.loads(authResponse.text))
    token = "Bearer " + parsed_auth["Result"]["AccessToken"]

def pushOrder(item, items):
    itemNum = str(item)
    itemName = items[item].name
    itemPrice = str(items[item].price)
    payload = "{\n    \n  \"Orders\": [\n    {\n      \"IsClosed\": true,\n      \"OrderNumber\": \"string\",\n      \"OrderDateTime\": \"2019-10-27T00:38:56.555Z\",\n      \"OrderDueDateTime\": \"2019-10-27T00:38:56.555Z\",\n      \"IsPaid\": true,\n      \"Customer\": {\n        \"CustomerId\": 0,\n        \"CustomerName\": \"string\",\n        \"Email\": \"string\",\n        \"PhoneNumber\": \"string\",\n        \"Address1\": \"string\",\n        \"Address2\": \"string\",\n        \"Address3\": \"string\",\n        \"City\": \"string\",\n        \"State\": \"string\",\n        \"ZipCode\": \"string\"\n      },\n      \"CustomerId\": 0,\n      \"CustomerName\": \"string\",\n      \"Email\": \"string\",\n      \"PhoneNumber\": \"string\",\n      \"TableReference\": \"string\",\n      \"TaxAmount\": 0,\n      \"TipAmount\": 0,\n      \"LineItems\": [\n        {\n          \"ExternalItemId\": \"" + itemNum +  "\",\n        \n          \"ItemName\": \"" + itemName + "\",\n          \"Quantity\": 1,\n          \"UnitPrice\": " + itemPrice +  ",\n          \"UnitSellPrice\": " + itemPrice + ",\n          \"ExtendedSellPrice\": " + itemPrice + ",\n          \n          \"Notes\": [\n            \"string\"\n          ],\n          \"BagName\": \"string\"\n        }\n      ],\n      \"Notes\": [\n        \"string\"\n      ],\n      \"KitchenLeadTimeInMinutes\": 0,\n      \"SkipReceipt\": true,\n      \"SkipKitchen\": true\n    }\n  ],\n  \"SourceApplicationName\": \"string\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)

@app.route("/")
def input():
    return render_template('input.html')

@app.route("/home")
def home():
    return render_template('home.html',diseaseList=diseaseList)


@app.route("/shop")
def shop():
    form = ButtonForm()
    return render_template('shop.html', items=itemAPI.createItemDictFromCSV(), form=form, disease = currDisease[len(currDisease) -  1], designated=itemAPI.loadModelDict())

@app.route("/diseasePlaceholder")
def diseasePlaceholder():
    disease = request.args.get('disease')
    currDisease.append(disease)
    return shop()

@app.route("/addToCart")
def addToCart():
	item_id = request.args.get('item_id')
	cartList.append(int(item_id))
	print(cartList)

	return shop()

@app.route("/checkout")
def checkout():
    items = itemAPI.createIDDictFromCSV()
    for item in cartList:
        if item < 28:
            pushOrder(item, items)
    cartList.clear()

    return shop()

@app.route("/cart")
def cart():
	return render_template('cart.html', items = itemAPI.createIDDictFromCSV(), docs = docAPI.createDocIDDictFromCSV(),cartList = cartList)

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
