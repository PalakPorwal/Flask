"""
from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "hello world"

if __name__== "__main__":
    app.run()
    
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    items.append(data)
    return jsonify({'message': 'Item added!'})

if __name__ == '__main__':
    app.run(debug=True)
