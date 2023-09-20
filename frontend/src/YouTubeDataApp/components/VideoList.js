// components/VideoList.js
import React, { useEffect, useState } from 'react';

function VideoList() {
    const [videos, setVideos] = useState([]);

    useEffect(() => {
        // Fetch data from the Django API endpoint
        fetch('/api/fetch-youtube-data/')
            .then((response) => response.json())
            .then((data) => setVideos(data))
            .catch((error) => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h2>YouTube Videos</h2>
            <ul>
                {videos.map((video) => (
                    <li key={video.video_id}>
                        <h3>{video.title}</h3>
                        <p>{video.description}</p>
                        <p>Date: {video.publication_date}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default VideoList;
