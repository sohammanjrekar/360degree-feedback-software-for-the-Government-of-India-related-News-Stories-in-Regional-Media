// Your React component file

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ScrapeNewsComponent() {
    const [scrapedData, setScrapedData] = useState([]);

    useEffect(() => {
        // Make an Axios GET request to the Django API endpoint
        axios.get('/api/scrape-news/')
            .then((response) => {
                setScrapedData(response.data);
            })
            .catch((error) => {
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <div>
            <h2>Scraped Data</h2>
            <ul>
                {scrapedData.map((item) => (
                    <li key={item.id}>{item.title}</li>
                ))}
            </ul>
        </div>
    );
}

export default ScrapeNewsComponent;
