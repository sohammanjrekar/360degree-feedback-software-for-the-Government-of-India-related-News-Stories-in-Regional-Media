// components/NewsList.js
import React, { useEffect, useState } from 'react';

function NewsList() {
    const [news, setNews] = useState([]);

    useEffect(() => {
        // Fetch data from the Django API endpoint
        fetch('/api/scrape-news/')
            .then((response) => response.json())
            .then((data) => setNews(data))
            .catch((error) => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h2>News Articles</h2>
            <ul>
                {news.map((article) => (
                    <li key={article.id}>
                        <h3>{article.title}</h3>
                        <p>{article.content}</p>
                        <p>Source: {article.source}</p>
                        <p>Date: {article.publication_date}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default NewsList;
