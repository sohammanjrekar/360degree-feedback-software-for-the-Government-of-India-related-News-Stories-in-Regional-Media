// Your React component file

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function FetchYouTubeDataComponent() {
    const [youtubeData, setYouTubeData] = useState([]);

    useEffect(() => {
        // Make an Axios GET request to the Django API endpoint
        axios.get('/api/fetch-youtube-data/')
            .then((response) => {
                setYouTubeData(response.data);
            })
            .catch((error) => {
                console.error('Error fetching YouTube data:', error);
            });
    }, []);

    return (
        <div>
            <h2>YouTube Data</h2>
            <ul>
                {youtubeData.map((item) => (
                    <li key={item.id}>{item.title}</li>
                ))}
            </ul>
        </div>
    );
}

export default FetchYouTubeDataComponent;
