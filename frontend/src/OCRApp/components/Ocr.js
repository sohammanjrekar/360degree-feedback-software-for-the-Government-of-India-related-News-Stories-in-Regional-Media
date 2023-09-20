// Your React component file

import React, { useState } from 'react';
import axios from 'axios';

function PerformOCRComponent() {
    const [extractedText, setExtractedText] = useState('');
    const [selectedImage, setSelectedImage] = useState(null);

    const handleImageChange = (event) => {
        setSelectedImage(event.target.files[0]);
    };

    const performOCR = () => {
        const formData = new FormData();
        formData.append('image', selectedImage);

        axios.post('/api/perform-ocr/', formData)
            .then((response) => {
                setExtractedText(response.data.text);
            })
            .catch((error) => {
                console.error('Error performing OCR:', error);
            });
    };

    return (
        <div>
            <input type="file" accept="image/*" onChange={handleImageChange} />
            <button onClick={performOCR}>Perform OCR</button>
            <div>
                <h2>Extracted Text</h2>
                <p>{extractedText}</p>
            </div>
        </div>
    );
}

export default PerformOCRComponent;
