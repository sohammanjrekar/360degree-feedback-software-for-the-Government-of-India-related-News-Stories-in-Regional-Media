// src/App.js
import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [cleanedText, setCleanedText] = useState('');

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append('image', selectedFile);

    try {
      const response = await fetch('http://localhost:8000/api/ocr-translation/', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setCleanedText(data.cleaned_text);
      } else {
        console.error('Error:', response.statusText);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <h1>OCR and Translation</h1>
      <input type="file" accept=".png, .jpg, .jpeg" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      {cleanedText && (
        <div>
          <h2>Cleaned Text</h2>
          <p>{cleanedText}</p>
        </div>
      )}
    </div>
  );
}

export default App;
