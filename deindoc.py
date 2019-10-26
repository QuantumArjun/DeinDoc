from flask import render_template, url_for, flash, redirect, request
import itemAPI
from forms import ButtonForm
import json
import requests
import http.client
app = Flask(__name__)


cartList = []

api_token = "gAAAAHIHg3TBY-z_dHiJxzMC2D3bKccwl1qA2l57KEpjiIlIB1R-EBRXiM7eFEUC-exTUCZPO5jinpRUgQl3fdxPeYZMRIHfGL6zItdp976F8M7KVIVF6LTosnUCzjR2T7eHwtvR8CTXhypo0OiZA6BxEQw-hh3x3bZFufaBm8WuLacO9AAAAIAAAACO6-ZxkFpS15OAl_RvlsxrgTYO_6ZhkLJseJgojCwxxAy-WJ4512VcrtP_JSTw2lTDJwz4tptYoBpjKC9wA84XxKPY2ROGv1Lw88dw4BVytidEJaVJC-HDrogxmLx9J_shXR0HXkK_vPUmG1bcLbawGtBfQQdatGY1ZSifYPD3b2qdyHmDbqhZSJuxwPVpsmh0cWMNgjQNG3s1x6SUtM_tlbKBlayh6oTbsdrtXy7lLBSDuGDsxWTrZ8pOWtLF9nWTz8Kfy4JaJ_twaGvHoxiLhiN3SD7zHwAfu1PNZOX_zDgP9hAwgMLTLj-bZt9xKh8"
client_id = "gt_552463"
client_secret = "004e007a-004a-0035-4b00-740033006800"

headers = {'Authorization': 'Bearer {0}'.format(api_token)}


conn = http.client.HTTPSConnection("gateway-staging.ncrcloud.com")

payload = "{\"fulfillment\":{\"address\":{\"type\":\"Business\",\"typeLabel\":\"String\",\"line1\":\"String\",\"line2\":\"String\",\"city\":\"String\",\"state\":\"String\",\"country\":\"String\",\"postalCode\":\"String\",\"coordinates\":{\"latitude\":33.6817952,\"longitude\":-84.4239568},\"crossStreets\":[{\"name\":\"Peachtree St\",\"lineId\":\"String\"}],\"notes\":\"String\",\"businessInfo\":{\"name\":\"String\",\"department\":\"String\"}},\"leadTimes\":[{\"type\":\"Transit\",\"typeLabel\":\"String\",\"interval\":6,\"intervalUnits\":\"Seconds\",\"lineId\":\"String\"}],\"notes\":\"String\",\"pickupDate\":\"2017-07-06T21:03:46.514Z\",\"pickupLocation\":\"String\",\"fulfillmentTime\":\"2018-01-31T12:34:56.789Z\",\"type\":\"Delivery\",\"typeLabel\":\"String\",\"autoRelease\":false},\"fees\":[{\"type\":\"None\",\"typeLabel\":\"String\",\"provider\":\"String\",\"amount\":38.1,\"override\":false,\"lineId\":\"String\"}],\"orderLines\":[{\"comments\":\"String\",\"description\":\"String\",\"extendedAmount\":43.45,\"itemType\":\"String\",\"notes\":[{\"type\":\"Substitutions\",\"typeLabel\":\"String\",\"value\":\"String\",\"lineId\":\"String\"}],\"parentLineId\":\"String\",\"priceModifiers\":[{\"amount\":23,\"description\":\"String\",\"referenceId\":\"String\",\"lineId\":\"String\"}],\"productId\":{\"type\":\"String\",\"value\":\"String\"},\"quantity\":{\"unitOfMeasure\":\"EA\",\"unitOfMeasureLabel\":\"String\",\"value\":64.75},\"substitutionAllowed\":false,\"taxes\":[{\"amount\":35.35,\"code\":\"String\",\"isIncluded\":false,\"percentage\":17.35,\"lineId\":\"String\"}],\"unitPrice\":48.1,\"scanData\":\"String\",\"supplementalData\":\"String\",\"modifierCode\":\"String\",\"linkGroupCode\":\"String\",\"lineReplaced\":\"String\",\"fulfillmentResult\":\"Replaced\",\"groupMemberId\":\"String\",\"overridePrice\":false,\"lineId\":\"String\"}],\"payments\":[{\"amount\":44.5,\"description\":\"String\",\"gratuity\":61.5,\"referenceId\":\"String\",\"status\":\"String\",\"type\":\"AccountsReceivable\",\"subType\":\"String\",\"maskedPAN\":\"String\",\"token\":\"String\",\"payBalance\":false,\"accountNumber\":\"String\",\"expiration\":{\"month\":31,\"year\":31},\"lineId\":\"String\"}],\"taxes\":[{\"amount\":93.2,\"code\":\"String\",\"description\":\"String\",\"isIncluded\":false,\"percentage\":28.15,\"source\":\"String\",\"active\":false,\"lineId\":\"String\"}],\"promotions\":[{\"referenceId\":\"String\",\"supportingData\":\"String\",\"amount\":39.55,\"numGuests\":74,\"orderLineGroups\":[{\"name\":\"String\",\"orderLineIds\":[\"String\"],\"lineId\":\"String\"}],\"adjustment\":{\"level\":\"ITEM\",\"type\":\"PROMO\"},\"lineId\":\"String\"}],\"additionalReferenceIds\":{},\"taxExempt\":false,\"taxExemptId\":\"String\",\"totalModifiers\":[{\"amount\":45.75,\"description\":\"String\",\"referenceId\":\"String\",\"lineId\":\"String\"}],\"partySize\":44,\"pickupContact\":{\"name\":\"String\",\"company\":\"String\",\"imageLink\":\"String\",\"phone\":\"String\",\"hasArrived\":false,\"vehicle\":{\"make\":\"Porsche\",\"model\":\"911 Turbo\",\"year\":\"2017\",\"color\":\"Silver\",\"licensePlate\":\"ABC1234\"}},\"checkInDetails\":{\"location\":\"Store Front\",\"application\":\"POS\",\"origin\":{\"type\":\"mobile or web\",\"id\":15},\"vector\":{\"type\":\"printer, queue, terminal, display or kiosk\",\"id\":30}},\"comments\":\"String\",\"channel\":\"PhoneIn\",\"currency\":\"String\",\"customer\":{\"id\":\"String\",\"externalIds\":[{\"type\":\"Reference\",\"typeLabel\":\"String\",\"value\":\"String\",\"lineId\":\"String\"}],\"name\":\"String\",\"firstName\":\"String\",\"lastName\":\"String\",\"phone\":\"String\",\"phoneExtension\":\"String\",\"email\":\"String\"},\"groupMembers\":[{\"name\":\"String\",\"firstName\":\"String\",\"lastName\":\"String\",\"externalIds\":{},\"lineId\":\"String\"}],\"errorDescription\":\"String\",\"owner\":\"String\",\"referenceId\":\"String\",\"source\":\"String\",\"status\":\"Canceled\",\"totals\":[{\"type\":\"Net\",\"value\":94.6,\"lineId\":\"String\"}]}"

headers = {
    'nep-source-organization': "String",
    'nep-correlation-id': "String",
    'nep-organization': "String",
    'nep-enterprise-unit': "String"
    }

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
    return render_template('shop.html', items=itemAPI.createItemDictFromCSV(), form=form)

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