// Your React component file

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function FetchTextAnalysisDataComponent() {
    const [textAnalysisData, setTextAnalysisData] = useState([]);

    useEffect(() => {
        // Make an Axios GET request to the Django API endpoint
        axios.get('/api/analyze-sentiment/')
            .then((response) => {
                setTextAnalysisData(response.data);
            })
            .catch((error) => {
                console.error('Error fetching text analysis data:', error);
            });
    }, []);

    return (
        <div>
            <h2>Text Analysis Data</h2>
            <ul>
                {textAnalysisData.map((item) => (
                    <li key={item.id}>{item.title}: {item.sentiment}</li>
                ))}
            </ul>
        </div>
    );
}

export default FetchTextAnalysisDataComponent;
