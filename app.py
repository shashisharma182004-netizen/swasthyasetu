from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Swasthya Setu API!"

@app.route('/disease_search', methods=['GET'])
def disease_search():
    disease = request.args.get('disease')
    # Implement your disease search logic here
    return jsonify({"message": f"Searching for information on {disease}."})

@app.route('/home_remedies', methods=['GET'])
def home_remedies():
    remedy = request.args.get('remedy')
    # Implement your home remedies logic here
    return jsonify({"message": f"Details about home remedy: {remedy}."})

@app.route('/api/resource', methods=['GET', 'POST'])
def api_resource():
    if request.method == 'GET':
        return jsonify({"message": "Resource fetched."})
    elif request.method == 'POST':
        data = request.json
        return jsonify({"message": "Data received.", "data": data})

if __name__ == '__main__':
    app.run(debug=True)