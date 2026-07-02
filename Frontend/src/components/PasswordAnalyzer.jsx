import { useState } from "react";
import API from "../services/api";
import "../styles/PasswordAnalyzer.css";
import StrengthBar from "./StrengthBar";

function PasswordAnalyzer() {
  const [password, setPassword] = useState("");
  const [result, setResult] = useState(null);
  const [showPassword, setShowPassword] = useState(false);
  const analyzePassword = async () => {
    try {
      const response = await API.post("/analyze-password", {
        password,
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Could not connect to backend.");
    }
  };

 return (
  <div className="analyzer-card">
    <input
      type={showPassword ? "text" : "password"}
      placeholder="Enter your password..."
      value={password}
      onChange={(e) => setPassword(e.target.value)}
    />
    <button
  className="toggle-btn"
  onClick={() => setShowPassword(!showPassword)}
>
  {showPassword ? "Hide Password" : "Show Password"}
    </button>

    <button onClick={analyzePassword}>
      Analyze Password
    </button>

    {result && (
      <div className="result-card">
        <h2>Analysis Result</h2>
           <StrengthBar score={result.score} />
        <p><strong>Score:</strong> {result.score}/100</p>
        <p><strong>Strength:</strong> {result.strength}</p>
        <p><strong>Entropy:</strong> {result.entropy} bits</p>
        <p><strong>Crack Time:</strong> {result.crack_time}</p>
        <p><strong>Length:</strong> {result.length}</p>

        <h3>Suggestions</h3>

        <ul>
          {result.suggestions.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
    )}
  </div>
);
}
export default PasswordAnalyzer;