from flask import Flask, request, jsonify
from models.joke_model import Joke

app = Flask(__name__)
app.secret_key="abcd" # This is only needed because I am using sessions. It is not required for the API to work.

#CORS - This allows the React app to connect to the API.
from flask_cors import CORS
CORS(app, support_credentials=True)

# For simplicity, I put all the routes here.
@app.route('/', methods=['GET'])          
def get_all_jokes():
    jokes = Joke.all()
    jokes_converted_to_json = [joke.to_json() for joke in jokes]
    return jsonify(jokes_converted_to_json), 200

@app.route('/', methods=['POST'])
def create_joke():
    data = request.json # extract the data submitted from the request. Handle EXACTLY like you do request.form.

    joke = Joke.create(data)
    return jsonify(joke.to_json()), 201

@app.route('/<int:id>', methods=['GET'])
def get_joke(id):
    joke = Joke.get_by_id(id)
    return jsonify(joke.to_json()), 200

@app.route('/<int:id>', methods=['PUT'])
def update_joke(id):
    data = request.json
    joke = Joke.update(id, data)
    return jsonify(joke.to_json()), 200

@app.route('/<int:id>', methods=['DELETE'])
def delete_joke(id):
    Joke.delete(id)
    return jsonify({}), 204

if __name__=="__main__":    
    app.run(debug=True)    

