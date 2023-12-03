# Using the Microsoft Azure Text Analytics API for Sentiment Analysis #

Sentiment analysis is the process of determining the sentiment or emotional tone of a piece of text. The Microsoft Azure Text Analytics API provides a powerful and easy-to-use solution for performing sentiment analysis on text data. In this guide, I will walk you through the process of using the Text Analytics API for sentiment analysis in Python.

#### Prerequisites

Before you can start using the Microsoft Azure Text Analytics API, you'll need to complete the following steps:

1. Sign up for Microsoft Azure: If you don't already have an account, you'll need to sign up for Microsoft Azure. Visit the Azure website and follow the instructions to create a new account.

2. Create a new Text Analytics resource: Once you have an Azure account, create a new Text Analytics resource. This resource will provide you with the necessary credentials and endpoints to access the Text Analytics API. To create a new resource, navigate to the Azure portal, click on "Create a resource," search for "Text Analytics," and follow the prompts to create a new resource.

3. Get your API key: After creating the Text Analytics resource, obtain your API key. This key is used to authenticate your requests to the Text Analytics API. To get your API key, go to the Azure portal, navigate to your Text Analytics resource, and look for the "Keys and Endpoint" section. Copy the value of the "Key1" field, as you'll need it later.

4. Install the Azure SDK for Python: To interact with the Text Analytics API in Python, you'll need to install the Azure SDK for Python. Open your terminal or command prompt and run the following command:

   ```
   pip install azure-ai-textanalytics
   ```

#### Getting Started with Sentiment Analysis

Now that you have completed the prerequisites, you can start using the Text Analytics API for sentiment analysis. Here are the steps to follow:

1. Import the necessary modules: In your Python script, import the necessary modules from the Azure SDK for Python. Here's an example:

   ```python
   from azure.ai.textanalytics import TextAnalyticsClient
   from azure.core.credentials import AzureKeyCredential
   ```

2. Create a Text Analytics client: Next, create an instance of the TextAnalyticsClient class using your API key and endpoint. Here's an example:

   ```python
   endpoint = "https://<your-text-analytics-endpoint>"
   credential = AzureKeyCredential("<your-api-key>")
   client = TextAnalyticsClient(endpoint, credential)
   ```

3. Analyze sentiment: Now you're ready to analyze sentiment using the Text Analytics API. You can pass a list of text documents to the `analyze_sentiment` method of the TextAnalyticsClient class. Here's an example:

   ```python
   documents = [
       "I love this product!",
       "This movie was terrible.",
       "The customer service was excellent."
   ]

   response = client.analyze_sentiment(documents)
   ```

4. Process the response: The `analyze_sentiment` method will return a response object that contains the sentiment analysis results for each document. You can iterate over the response to access the sentiment scores and other information. Here's an example:

   ```python
   for document in response:
       print("Document sentiment: {}".format(document.sentiment))
       print("Overall scores: positive={:.2f}; neutral={:.2f}; negative={:.2f}".format(
           document.confidence_scores.positive,
           document.confidence_scores.neutral,
           document.confidence_scores.negative
       ))
   ```

By following these steps, you can easily integrate sentiment analysis into your Python applications using the Microsoft Azure Text Analytics API.

Remember to refer to the official Microsoft Azure documentation for more detailed information and additional features of the Text Analytics API. Happy coding!

**Note:** The information provided in this response is based on my understanding of the topic. Please verify the details from the official documentation or relevant sources.







# Certainly! Here's the complete code that scrapes Play Store app reviews and performs sentiment analysis using Python: #

```python
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Install NLTK dependencies
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Scrape Play Store app reviews
url = 'https://play.google.com/store/apps/details?id=com.tencent.ig'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
reviews = soup.find_all('div', {'class': 'review-body'})

# Process the reviews
tokenized_reviews = [word_tokenize(review.text) for review in reviews]

stop_words = set(stopwords.words('english'))
filtered_reviews = [[word for word in review if word.lower() not in stop_words] for review in tokenized_reviews]

sia = SentimentIntensityAnalyzer()
sentiment_scores = [sia.polarity_scores(' '.join(review)) for review in filtered_reviews]

# Analyze the sentiment scores
positive_reviews = [score for score in sentiment_scores if score['compound'] > 0]
negative_reviews = [score for score in sentiment_scores if score['compound'] < 0]
neutral_reviews = [score for score in sentiment_scores if score['compound'] == 0]

# Calculate the overall sentiment score
overall_sentiment_score = sum(score['compound'] for score in sentiment_scores) / len(sentiment_scores)

# Print the results
print("Total reviews:", len(sentiment_scores))
print("Positive reviews:", len(positive_reviews))
print("Negative reviews:", len(negative_reviews))
print("Neutral reviews:", len(neutral_reviews))
print("Overall sentiment score:", overall_sentiment_score)
```

Make sure to replace `'https://play.google.com/store/apps/details?id=com.example.app'` with the URL of the Play Store app you want to scrape reviews from.
https://play.google.com/store/apps/details?id=com.tencent.ig

This code imports the necessary libraries, sends an HTTP GET request to the Play Store app page, parses the HTML response using BeautifulSoup, extracts the reviews, tokenizes the text, removes stopwords, performs sentiment analysis using the VADER sentiment analyzer from NLTK, and calculates the overall sentiment score. Finally, it prints the results, including the total number of reviews, the number of positive, negative, and neutral reviews, and the overall sentiment score.

Remember to install the required libraries using `pip install requests beautifulsoup4 nltk` before running the code.

Let me know if you have any further questions!
