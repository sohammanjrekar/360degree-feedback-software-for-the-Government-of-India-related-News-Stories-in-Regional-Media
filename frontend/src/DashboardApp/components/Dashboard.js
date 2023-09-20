// src/components/Dashboard.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Dashboard() {
    const [dashboardData, setDashboardData] = useState({ news_articles: [], videos: [] });

    useEffect(() => {
        // Fetch data from the Django backend
        axios.get('/api/dashboard-data/')
            .then((response) => {
                setDashboardData(response.data);
            })
            .catch((error) => {
                console.error('Error fetching dashboard data:', error);
            });
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            <h2>News Articles</h2>
            <ul>
                {dashboardData.news_articles.map((article) => (
                    <li key={article.id}>{article.title}</li>
                ))}
            </ul>
            <h2>Videos</h2>
            <ul>
                {dashboardData.videos.map((video) => (
                    <li key={video.id}>{video.title}</li>
                ))}
            </ul>
        </div>
    );
}

export default Dashboard;
