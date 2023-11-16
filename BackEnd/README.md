Sure! Here is the code step by step, properly formatted and indented:

```python
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_text():
    payload = request.get_json()
    text = payload['text']

    # Make a POST request to the Microsoft Azure Text Analytics API
    azure_api_url = "<your-azure-api-url>"
    azure_api_key = "<your-azure-api-key>"
    azure_headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': azure_api_key
    }
    azure_data = {
        'documents': [
            {
                'id': '1',
                'text': text
            }
        ]
    }
    azure_response = requests.post(azure_api_url, headers=azure_headers, json=azure_data)
    azure_results = azure_response.json()

    # Make a GET request to the Play Store API
    play_store_api_url = "<play-store-api-url>"
    play_store_response = requests.get(play_store_api_url)
    play_store_results = play_store_response.json()

    # Process the results from both APIs and create a response dictionary
    response = {
        'text': text,
        'azure_results': azure_results,
        'play_store_results': play_store_results
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
```

To run the Flask application, make sure you have Flask installed. If not, you can install it using the command `pip install flask`. Save the code in a file named `app.py` and run it using the command `python app.py`. The application will start running on `http://localhost:5000`.

You can test the application by sending a POST request to `http://localhost:5000/analyze` with the following JSON payload:

```json
{
  "text": "This is a sample text to analyze."
}
```

The application will call the Microsoft Azure Text Analytics API and the Play Store API, process the results, and return a JSON response containing the results from both APIs.

That's it! You have successfully created a Flask application that interacts with APIs. Feel free to modify the code to suit your specific requirements. Happy coding!
