from flask import Flask, jsonify, render_template, request, url_for
import config
from utils import SelPrice
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("Welcome to Car Price Prediction")
    return render_template("home.html")


@app.route("/predict_price",methods=["GET","POST"])
def prediction():
    if request.method == 'POST':
        data = request.form
        
        print('data :',data)

        sell_price = SelPrice(data)
        price = sell_price.predict_selling_price()
        return render_template("home.html",prediction =price)
        #return jsonify ({"Price :":f"Your Car Price will be {price} /- lakh Only"})


if __name__ == "__main__":
    app.run(host ="0.0.0.0",port=config.PORT_NUMBER)