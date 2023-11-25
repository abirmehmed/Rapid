import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const SentimentAnalysis = () => {
  const [inputText, setInputText] = useState('');
  const [sentimentData, setSentimentData] = useState([]);

  useEffect(() => {
    if (inputText) {
      fetchSentimentAnalysis();
    }
  }, [inputText]);

  const fetchSentimentAnalysis = async () => {
    try {
      const response = await axios.post('/api/sentiment', { text: inputText });
      setSentimentData(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text for sentiment analysis..."
      />
      <Line data={sentimentData} />
    </div>
  );
};

export default SentimentAnalysis;
