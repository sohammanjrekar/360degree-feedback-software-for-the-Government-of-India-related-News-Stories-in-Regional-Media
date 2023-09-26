import React, { useState } from 'react';
import axios from 'axios';

function OcrTranslate() {
    const [translatedText, setTranslatedText] = useState('');
    const [file, setFile] = useState(null);

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        setFile(selectedFile);
    };

    const handleUpload = () => {
        if (!file) {
            console.error('No file selected.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        axios
            .post('http://localhost:8000/ocr/api/ocr_and_translate/', formData, {
                withCredentials: true, // Include credentials if needed
                headers: {
                    'Content-Type': 'multipart/form-data', // Set the content type
                    
       
                },
            })
            .then((response) => {
                setTranslatedText(response.data.translated_text);
            })
            .catch((error) => {
                console.error(error);
            });
    };

    return (
        <div>
            <h1>Upload an image or PDF for OCR and Translation</h1>
            <input type="file" accept="image/*, application/pdf" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
            {translatedText && (
                <div>
                    <h2>Translated Text:</h2>
                    <p>{translatedText}</p>
                </div>
            )}
        </div>
    );
}

export default OcrTranslate;
