import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Use Routes instead of Route
import OcrTranslate from './OCRApp/components/Ocr';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>My OCR and Translation App</h1>
        </header>
        <Routes>
          {/* Define your routes here */}
          <Route path="/ocr-translate" element={<OcrTranslate />} /> {/* Use "element" prop */}
          {/* Add more routes as needed */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
