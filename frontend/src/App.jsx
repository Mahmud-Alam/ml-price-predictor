import React, { useState } from "react";
import axios from "axios";

function App() {
  const [area, setArea] = useState("");
  const [price, setPrice] = useState(null);

  const handlePredict = async () => {
    try {
      const res = await axios.post("http://localhost:5000/predict", {
        area: parseFloat(area),
      });
      setPrice(res.data.predicted_price);
    } catch (error) {
      alert("Prediction failed!");
    }
  };

  return (
    <main>
      <div className="container">
        <h2>🏠 House Price Predictor</h2>
        <input
          className="input-field"
          type="number"
          placeholder="Enter area in sq.ft"
          value={area}
          onChange={(e) => setArea(e.target.value)}
        />
        <button className="btn" onClick={handlePredict}>
          Predict
        </button>
        {price && (
          <div className="result-text">
            <strong>Predicted Price:</strong> ${price}
          </div>
        )}
      </div>
    </main>
  );
}

export default App;
