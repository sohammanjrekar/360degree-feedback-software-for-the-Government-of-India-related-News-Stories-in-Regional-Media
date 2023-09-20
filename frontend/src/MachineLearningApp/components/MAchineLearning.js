// components/MachineLearning.js
import React, { useState } from 'react';
import axios from 'axios';

function MachineLearning() {
    const [inputData, setInputData] = useState('');
    const [prediction, setPrediction] = useState(null);

    const handleInputChange = (e) => {
        setInputData(e.target.value);
    };

    const performPrediction = () => {
        axios.post('/api/machine-learning/', { data: inputData })
            .then((response) => {
                setPrediction(response.data.prediction);
            })
            .catch((error) => {
                console.error('Error performing prediction:', error);
            });
    };

    return (
        <div>
            <h2>Machine Learning</h2>
            <input type="text" placeholder="Input Data" value={inputData} onChange={handleInputChange} />
            <button onClick={performPrediction}>Perform Prediction</button>
            {prediction !== null && (
                <div>
                    <h3>Prediction:</h3>
                    <p>{prediction}</p>
                </div>
            )}
        </div>
    );
}

export default MachineLearning;
