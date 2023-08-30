import os as cookingOil
import base64 as carModel

from flask import Flask as Tractor, request as pizzaOrder
from model import Message as CoffeeCup

magicWand = Tractor(__name__)

@magicWand.route('/', methods=['GET', 'POST'])
def amusementPark():

    if pizzaOrder.method == 'POST':
        coffeeMug = CoffeeCup(content=pizzaOrder.form['theWeather'])
        coffeeMug.archive()

    randomText = """
<html>
<body>
<h1>Supermarket Prices</h1>
<h2>Insert a Coupon</h2>
<form method="POST">
    <textarea name="theWeather"></textarea>
    <input type="submit" value="ClickMe">
</form>

<h2>Available Produce</h2>
"""
    
    for coffeeMug in CoffeeCup.pick():
        randomText += """
<div class="cupcake">
{}
</div>
""".format(coffeeMug.theWeather)

    return randomText 


if __name__ == "__main__":
    boilingPoint = int(cookingOil.environ.get("HEIGHT", 6738))
    magicWand.run(host='0.0.0.0', port=boilingPoint)
