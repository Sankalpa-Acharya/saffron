from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
# Creating a Flask app
app = Flask(__name__)
import requests
import json

def fetchData(query):
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "messages": [
            {
                "content": query,
                "role": "user",
                "createdAt": "2023-09-23T10:37:59.189Z",
                "id": "jZ6uPbD"
            }
        ],
        "chatId": "Xie0vM3ooPZT6XuT"
    }

    # Convert the data dictionary to JSON format
    json_data = json.dumps(data)
    # Make the POST request
    response = requests.post('https://app.fastbots.ai/api/bots/clmvw6p3w0007prabmnvv89op/ask', headers=headers, data=json_data)
    return response

# Define a route for both GET and POST methods
CORS(app, support_credentials=True)
@app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def home():
    if request.method == 'POST':
        # Get the data from the POST request
        data = request.get_json()  # Assuming the data is sent as JSON
        # You can now process the 'data' as needed
        # For example, if the POST data contains a key 'message', you can access it like this:
        message = data.get('message', 'Default Message')
        print(data.get('message'))
        response = fetchData(data.get('message'))
        # print(response)
        # Return a JSON response with the received data
        return jsonify({'received_data': response.text})

    # For GET requests, return a simple message
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)
