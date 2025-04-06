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
    <main className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="bg-white p-6 rounded-xl shadow-lg w-full max-w-md">
        <h2 className="text-2xl font-bold mb-4 text-center">
          🏠 House Price Predictor
        </h2>
        <div className="flex items-center gap-2 mb-4">
          <input
            type="number"
            placeholder="Enter area in sq.ft"
            value={area}
            onChange={(e) => setArea(e.target.value)}
            className="flex-1 border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
          <button
            onClick={handlePredict}
            className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
          >
            Predict
          </button>
        </div>
        {price && (
          <div className="text-green-700 font-semibold text-lg text-center">
            Predicted Price: ${price}
          </div>
        )}
      </div>
    </main>
  );
}

export default App;
