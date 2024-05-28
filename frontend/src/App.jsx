import { useState } from "react";
import axios from 'axios';
import "./App.css";

function App() {
  const [cgpa, setCgpa] = useState('');
  const [iq, setIq] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/predict', {
        cgpa: parseFloat(cgpa),
        iq: parseInt(iq)
      });
      setMessage(response.data.message);
    } catch (error) {
      console.error('Error making prediction:', error);
    }
  };

  return (
    <div className="App">
      <h1>Student Placement Prediction</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            CGPA:
            <input
              type="number"
              step="0.01"
              value={cgpa}
              onChange={(e) => setCgpa(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            IQ:
            <input
              type="number"
              value={iq}
              onChange={(e) => setIq(e.target.value)}
              required
            />
          </label>
        </div>
        <button type="submit">Predict</button>
      </form>
      {message && (
        <div>
          <h2>Prediction Result</h2>
          <p>{message}</p>
        </div>
      )}
    </div>
  );
}

export default App;
