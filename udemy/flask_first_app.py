from flask import Flask, jsonify, request


app = Flask(__name__)  #creating an object using Flask class with a unique name


# stores = [
#     {
#         'name': 'First Store',
#         'items':[
#             {
#                 'name': 'Together for Good',
#                 'price': 15.99
#             },
#             {
#                 'name': 'Prayer of the Pious',
#                 'price': 9.99
#             }
#
#
#
#         ]
#     },
#
#     {
#         'name': 'Second Store',
#         'items': [
#             {
#                 'name': 'My Lost Land',
#                 'price': 13.99
#             },
#             {
#                 'name': 'Lemon Tree',
#                 'price': 19.99
#             }
#
#         ]
#     },
#
#
# ]

stores = [{
    'name': 'First Store LLC',
    'items': [{'name': 'my item', 'price': 15.99}]
      }
]


@app.route('/tugba')  # end point. On the browser: http://127.0.0.1:5000/tugba PS: by default, route() uses GET verb.
def tugbas_page():  # controller  debug ile ilk dustugum yer
    return "Hello Tugba!"


@app.route('/erdem/sum/<int:num1>/<int:num2>')  # end point. On the browser: http://127.0.0.1:5000/erdem
def erdems_page(num1,num2):
    sumoftwo = num1 + num2
    return jsonify({"sum": str(sumoftwo)})


@app.route('/sum', methods=['POST'])
def sum_func():
    return "10"


@app.route('/store')  # Returns all stores
def get_all_stores():
    return jsonify({'stores': stores})


@app.route('/store', methods=['POST'])  # Creates a new store , adds to the existing store list, and returns all stores
def create_store():
    request_data = request.get_json()  # Reads the data sent over via json body
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify({"store": stores})


@app.route('/store/<string:name>')
def get_store(name):  # Checks if a specific store exists or not
    for store in stores:
        if store['name'] == name:
            return jsonify({'message': 'This store exists'})
    return jsonify({'message': 'Store not found'})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in__store(name):
    request_data = request.get_json()
    for store in stores:
        if name == store['name']:
            new_item = {
                "name": request_data['name'],
                "price": request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({"stores": stores})


@app.route('/store', methods=['DELETE'])
def delete_store():
    request_data = request.get_json()
    for store in stores:
        if store['name'] == request_data['name']:
            del store
            return jsonify({'message': 'Store deleted'})
    return jsonify({'message': 'Store not found'})






app.run(port = 5000)