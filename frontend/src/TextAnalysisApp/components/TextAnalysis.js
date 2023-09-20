// components/TextAnalysis.js
import React, { useState } from 'react';
import axios from 'axios';

function TextAnalysis() {
    const [text, setText] = useState('');
    const [sentiment, setSentiment] = useState(null);

    const analyzeText = () => {
        axios.post('/api/analyze-sentiment/', { text })
            .then((response) => {
                setSentiment(response.data.sentiment);
            })
            .catch((error) => {
                console.error('Error analyzing text:', error);
            });
    };

    return (
        <div>
            <h2>Text Analysis</h2>
            <textarea
                placeholder="Enter text for analysis..."
                value={text}
                onChange={(e) => setText(e.target.value)}
            />
            <button onClick={analyzeText}>Analyze</button>
            {sentiment && (
                <p>Sentiment: {sentiment}</p>
            )}
        </div>
    );
}

export default TextAnalysis;
