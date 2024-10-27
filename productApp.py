from flask import Flask, request,jsonify
app = Flask(__name__)
products=[{"id": 1,
          "name": "Bournvita",
          "description": "Milk"},
          {
          "id": 2,
          "title": "iPhone",
          "description": "Mobile"
        }]

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/listings',methods=['GET'])
def get_list():
    return products

@app.route('/product/<product_id>',methods=['GET'])
def find_product(product_id):
    product_id=int(product_id)
    for product in products:
        if product["id"]==product_id:
            return jsonify(product)
    return "not found"

@app.route('/addproduct',methods=['POST'])
def get_product():
    length=len(products)+1
    product=request.json
    product['id']=length
    products.append(product)
    return products

if __name__== '__main__':
    app.run(debug=True,port=5000)