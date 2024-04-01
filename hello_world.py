from flask import Flask, request, jsonify
import data

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome To my API</p>"

@app.route('/products')
def get_products():
    return data.products_data

@app.route('/categories')
def get_categories():
    return data.categories_data

@app.route('/brands')
def get_brands():
    return data.brands_data


@app.route('/brands', methods=['POST'])
def create_brands():
    brand_details = request.get_json()["brand_name"]
    data.brands_data.append(brand_details)
    return {"message":f"New brand {brand_details}Added successfully"}

@app.route('/categories', methods=['POST'])
def create_brands():
    category_details = request.get_json()["brand_name"]
    data.category_data.append(category_details)
    return {"message":f"New brand {category_details}Added successfully"}