"""
Jalen Banks
March 24th, 2026
Lab 15, RESTful API and unit test in a Flask App
"""

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory database (dictionary)
items = {}

@app.route('/')
def home():
    return render_template('index.html')

# Create an item
@app.route('/items', methods = ['POST'])
def create_item():
    # get_json method is used to read JSON data sent by the client in an HTTP request
    data = request.get_json()

    # Generate a new unique ID for the new item
    item_id = str(len(items)+1)
    
    # Add the data collected for the new item
    items[item_id] = data
    
    # jsonify converts a Python dictionary into a json response, and returns the status code as 201 (your request worked and new resource was created) 
    return jsonify({'id':item_id, 'item': data}), 201


# READ ALL ITEMS
@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)

# READ SINGLE ITEM
@app.route('/items/<item_id>', methods = ['GET', 'PUT', 'DELETE'])
def handle_item(item_id):
    item = items.get(item_id)
    # READ
    if request.method == 'GET':

        if not item :
            # 404 = server is reachable but the item you asked for doesn't exist
            return jsonify({'Error: "Item not found"'}), 404
    
        return jsonify(item)

    # UPDATE
    elif request.method == 'PUT':
        if not item:
            return render_template('error.html', message = "NOT FOUND", item = item), 404
        
        data = request.get_json()
        if not data:
            return jsonify({'error' : 'Invalid input'}), 400
        
        items[item_id] = data
        return render_template('update.html', item_id = item_id, item = data)
    
    # DELETE
    elif request.method == "DELETE":
        deleted_item = items.pop(item_id)
        return render_template("delete.html", item_id = item_id, deleted_item = deleted_item)
    



if __name__ == '__main__':
    app.run(debug=True)