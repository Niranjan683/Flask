## Put and Delete - HTTP verbs
## working with API's -- JSON

from  flask import Flask, jsonify , request

app=Flask(__name__)

## intial data in my todo list

items= [
    {'id':1, 'name': "Items1", 'description':"This is Item 1"},
    {'id':2, 'name': "Items2", 'description':"This is Item 2"}
]

@app.route('/')
def home():
    return "Welcom to the sample To Do list app"

# Get : Retrive all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

# get: rwtrve a specific ite by Id
@app.route('/items/<int:item_id>', methods = ['GET'])
def get_item(item_id):
    item = next ((item for item in items if item['id'] == item_id),None)
    if item is None:
        return jsonify({'error': 'item not found'})
    return jsonify (item)

#Post : create new task 
app.route('/items',method=['POST'])
def create_item():
    if not request.json  or not 'name' in request.json:
        return jsonify({"error": "item not found"})
    new_item={
        'id': items[1]['id']+1 if items else 1,
        'name': request.json['name'],
        "description": request.json['description']
    }

    items.append(new_item)

    return jsonify(new_item)

#Put : Update an existng item
@app.route('/items/<int:item_id>',methods= ['PUT'])

def update_item(item_id):
    item = next ((item for item in items if item['id'] == item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    item ['name'] = request.json.get('name',item['name'])
    item ['description'] = request.json.get('description',item['description'])
    return jsonify(item)

# Delete: delete an item 
@app.route('/items/<int:item_id>',methods= ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item[id] != item_id]
    return jsonify({"result":"Item deleted"})



if __name__=='__main__':
    app.run(debug=True)