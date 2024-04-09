import React, { useState } from 'react';
import './App.css';

function App() {
  const [sequence, setSequence] = useState('');
  const [predictedSST3Structure, setPredictedSST3Structure] = useState('');
  const [predictedSST8Structure, setPredictedSST8Structure] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Fetch the predicted secondary structure from the backend
  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ sequence: sequence.toUpperCase() }),
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();

	  // Update the state with the predicted secondary structure
      setPredictedSST3Structure(data.predicted_sst3_structure.replace(/\s/g, '').toUpperCase());
      setPredictedSST8Structure(data.predicted_sst8_structure.replace(/\s/g, '').toUpperCase());
    } catch (error) {
      console.error("Failed to fetch: ", error);
    } finally {
      setIsLoading(false);
    }
  };

  // Clear the input and output fields
  const handleClear = () => {
    setSequence('');
    setPredictedSST3Structure('');
    setPredictedSST8Structure('');
    setIsLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Secondary Protein Structure Prediction</h1>
        <form onSubmit={handleSubmit}>
          <textarea
            className="sequence-input"
            value={sequence}
            onChange={(e) => setSequence(e.target.value.toUpperCase())}
            placeholder="Enter amino acid sequence"
            rows="4"
            spellCheck="false"
          />
          <div className="buttons">
            <button type="submit" className="submit-btn" disabled={isLoading}>
              {isLoading ? 'Predicting...' : 'Predict'}
            </button>
            <button type="button" className="clear-btn" onClick={handleClear}>
              Clear
            </button>
          </div>
        </form>
        {isLoading && <div>Loading...</div>} {/* Display loading indicator */}
        {predictedSST3Structure && (
          <div className="output-box">
            <p>Predicted SST3 Structure: <span>{predictedSST3Structure}</span></p>
          </div>
        )}
        {predictedSST8Structure && (
          <div className="output-box">
            <p>Predicted SST8 Structure: <span>{predictedSST8Structure}</span></p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;


