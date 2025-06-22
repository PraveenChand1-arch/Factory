from flask import Flask, jsonify, request

app = Flask(__name__)
inventory = []

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.get_json()
    inventory.append(data)
    return jsonify({'message': 'Item added!'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
