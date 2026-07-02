import { useState, useEffect } from "react";
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
  useEffect(() => {
  if (!password) {
    setResult(null);
    return;
  }

  const timer = setTimeout(() => {
    analyzePassword();
  }, 400);

  return () => clearTimeout(timer);
}, [password]);

const getStrengthColor = () => {
  switch (result?.strength) {
    case "Very Strong":
      return "#16a34a";
    case "Strong":
      return "#22c55e";
    case "Moderate":
      return "#f59e0b";
    case "Weak":
      return "#ef4444";
    default:
      return "#6b7280";
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

{/*    <button onClick={analyzePassword}>
      Analyze Password
    </button> */}

    {result && (
      <div className="result-card">
        <h2>Analysis Result</h2>
           <StrengthBar score={result.score} />
        <div className="stats-grid">

  <div className="stat-box">
    <h4>Score</h4>
    <span>{result.score}/100</span>
  </div>

  <div className="stat-box">
  <h4>Strength</h4>

  <span
    style={{
      color: getStrengthColor(),
      fontWeight: "bold",
      fontSize: "22px",
    }}
  >
    {result.strength}
  </span>
  </div>

  <div className="stat-box">
    <h4>Entropy</h4>
    <span>{result.entropy} bits</span>
  </div>

  <div className="stat-box">
    <h4>Crack Time</h4>
    <span>{result.crack_time}</span>
  </div>
 
</div>
<h3>Security Checks</h3>

<div className="checks">

  <p>{result.has_uppercase ? "✅" : "❌"} Uppercase Letter</p>

  <p>{result.has_lowercase ? "✅" : "❌"} Lowercase Letter</p>

  <p>{result.has_number ? "✅" : "❌"} Number</p>

  <p>{result.has_special ? "✅" : "❌"} Special Character</p>

  <p>{result.has_repeated_characters ? "⚠️" : "✅"} Repeated Characters</p>

  <p>{result.has_sequential_pattern ? "⚠️" : "✅"} Sequential Pattern</p>

  <p>{result.has_keyboard_pattern ? "⚠️" : "✅"} Keyboard Pattern</p>

  <p>{result.is_common_password ? "⚠️" : "✅"} Common Password</p>

</div>
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