from flask import Flask, render_template, url_for, flash, redirect, request
import itemAPI
from forms import ButtonForm
import json
import requests
import http.client
app = Flask(__name__)

model = pickle.load(open('model.sav', 'rb'))

cartList = []

api_token = "gAAAAHIHg3TBY-z_dHiJxzMC2D3bKccwl1qA2l57KEpjiIlIB1R-EBRXiM7eFEUC-exTUCZPO5jinpRUgQl3fdxPeYZMRIHfGL6zItdp976F8M7KVIVF6LTosnUCzjR2T7eHwtvR8CTXhypo0OiZA6BxEQw-hh3x3bZFufaBm8WuLacO9AAAAIAAAACO6-ZxkFpS15OAl_RvlsxrgTYO_6ZhkLJseJgojCwxxAy-WJ4512VcrtP_JSTw2lTDJwz4tptYoBpjKC9wA84XxKPY2ROGv1Lw88dw4BVytidEJaVJC-HDrogxmLx9J_shXR0HXkK_vPUmG1bcLbawGtBfQQdatGY1ZSifYPD3b2qdyHmDbqhZSJuxwPVpsmh0cWMNgjQNG3s1x6SUtM_tlbKBlayh6oTbsdrtXy7lLBSDuGDsxWTrZ8pOWtLF9nWTz8Kfy4JaJ_twaGvHoxiLhiN3SD7zHwAfu1PNZOX_zDgP9hAwgMLTLj-bZt9xKh8"
client_id = "gt_552463"
client_secret = "004e007a-004a-0035-4b00-740033006800"

headers = {'Authorization': 'Bearer {0}'.format(api_token), 'Accept': 'application/json'}


conn = http.client.HTTPSConnection("api-reg.ncrsilverlab.com")

payload = "{ \
  \"Orders\": [ \
    { \
      \"IsClosed\": true, \
      \"OrderNumber\": \"string\",\
      \"OrderDateTime\": \"2019-10-26T23:49:56.932Z\",\
      \"OrderDueDateTime\": \"2019-10-26T23:49:56.932Z\", \
      \"IsPaid\": true,\
      \"Customer\": {\
        \"CustomerId\": 0,\
        \"CustomerName\": \"string\",\
        \"Email\": \"string\",\
        \"PhoneNumber\": \"string\",\
        \"Address1\": \"string\",\
        \"Address2\": \"string\",\
        \"Address3\": \"string\",\
        \"City\": \"string\",\
        \"State\": \"string\",\
        \"ZipCode\": \"string\"\
      },\
      \"CustomerId\": 0,\
      \"CustomerName\": \"string\",\
      \"Email\": \"string\",\
      \"PhoneNumber\": \"string\",\
      \"TableReference\": \"string\",\
      \"TaxAmount\": 0,\
      \"TipAmount\": 0,\
      \"LineItems\": [\
        {\
          \"ItemId\": 1,\
          \"ExternalItemId\": \"1711677\",\
          \"ItemName\": \"string\",\
          \"Quantity\": 1,\
          \"UnitPrice\": 0,\
          \"UnitSellPrice\": 0,\
          \"ExtendedSellPrice\": 0,\
          \"Modifiers\": [\
          ],\
          \"Notes\": [\
            \"string\" \
          ],\
          \"BagName\": \"string\"\
        }\
      ],\
      \"Notes\": [\
        \"string\" \
      ],\
      \"KitchenLeadTimeInMinutes\": 0,\
      \"SkipReceipt\": true,\
      \"SkipKitchen\": true,\
      \"Payments\": [\
        {\
          \"ExternalPaymentId\": \"string\"\
        }\
      ]\
    }\
  ],\
  \"SourceApplicationName\": \"string\"\
}"

conn.request("POST", "/order/orders", payload, headers)

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
