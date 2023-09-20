// src/components/Notification.js

import React, { useState } from 'react';
import axios from 'axios';

function Notification() {
    const [phone, setPhone] = useState('');
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');

    const handlePhoneChange = (e) => {
        setPhone(e.target.value);
    };

    const handleMessageChange = (e) => {
        setMessage(e.target.value);
    };

    const sendNotification = () => {
        axios.post('/api/notifications/', { phone_number: phone, message: message })
            .then((response) => {
                setResponse(response.data.message);
            })
            .catch((error) => {
                console.error('Error sending notification:', error);
            });
    };

    return (
        <div>
            <h2>Notification</h2>
            <input type="text" placeholder="Phone Number" value={phone} onChange={handlePhoneChange} />
            <input type="text" placeholder="Message" value={message} onChange={handleMessageChange} />
            <button onClick={sendNotification}>Send Notification</button>
            {response && (
                <div>
                    <h3>Response:</h3>
                    <p>{response}</p>
                </div>
            )}
        </div>
    );
}

export default Notification;
