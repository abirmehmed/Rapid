# app.py

from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_text():
    # Get the text from the request
    text = request.json['text']

    # Call the Microsoft Azure Text Analytics API
    azure_api_url = 'https://<your-azure-api-url>'
    azure_api_key = '<your-azure-api-key>'
    azure_headers = {'Ocp-Apim-Subscription-Key': azure_api_key}
    azure_data = {'documents': [{'id': '1', 'text': text}]}
    azure_response = requests.post(azure_api_url, headers=azure_headers, json=azure_data)
    azure_result = azure_response.json()

    # Call the Play Store API
    playstore_api_url = 'https://<play-store-api-url>'
    playstore_response = requests.get(playstore_api_url)
    playstore_result = playstore_response.json()

    # Process the results and return the response
    response = {
        'azure_result': azure_result,
        'playstore_result': playstore_result
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
