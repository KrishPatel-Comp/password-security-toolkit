import { useState, useEffect } from "react";
import API from "../services/api";
import "../styles/PasswordAnalyzer.css";
import StrengthBar from "./StrengthBar";
import { motion } from "framer-motion";
import { FiEye, FiEyeOff, FiLock } from "react-icons/fi";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";
import SecurityCheck from "./SecurityCheck";

function PasswordAnalyzer() {
  const [password, setPassword] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [history, setHistory] = useState([]);
  const analyzePassword = async () => {
  if (!password.trim()) {
    setResult(null);
    return;
  }

  setLoading(true);

  try {
    const response = await API.post("/analyze-password", {
      password,
    });

    setResult(response.data);
    setHistory(prev => {
  const updated = [
    {
      password,
      score: response.data.score,
      strength: response.data.strength,
    },
    ...prev,
  ];

  return updated.slice(0, 5);
});
  } catch (error) {
    console.error(error);
  } finally {
    setLoading(false);
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
 <motion.div
  className="analyzer-card"
  initial={{ opacity: 0, y: 40 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.6 }}
>
   <div className="input-container">
  <FiLock className="lock-icon" />

  <input
    type={showPassword ? "text" : "password"}
    placeholder="Enter your password..."
    value={password}
    onChange={(e) => setPassword(e.target.value)}
  />

  <button
    className="eye-btn"
    onClick={() => setShowPassword(!showPassword)}
  >
    {showPassword ? <FiEyeOff /> : <FiEye />}
  </button>
</div>

{/*    <button onClick={analyzePassword}>
      Analyze Password
    </button> */}
    {loading && (
  <div className="loading">
    Analyzing password...
  </div>
)}

    {result && (
      <div className="result-card">
        <h2>Analysis Result</h2>
           <StrengthBar score={result.score} />
        <div className="stats-grid">

  <div className="stat-box">
  <CircularProgressbar
    value={result.score}
    text={`${result.score}`}
    styles={buildStyles({
      textSize: "22px",
      pathColor:
        result.score >= 80
          ? "#22c55e"
          : result.score >= 60
          ? "#3b82f6"
          : result.score >= 40
          ? "#f59e0b"
          : "#ef4444",
      textColor: "#ffffff",
      trailColor: "#334155",
    })}
  />

  <h4 style={{ marginTop: "15px" }}>Score</h4>
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

<SecurityCheck
title="Uppercase Letter"
status={result.has_uppercase}
/>

<SecurityCheck
title="Lowercase Letter"
status={result.has_lowercase}
/>

<SecurityCheck
title="Number"
status={result.has_number}
/>

<SecurityCheck
title="Special Character"
status={result.has_special}
/>

<SecurityCheck
title="Repeated Characters"
status={result.has_repeated_characters}
warning={true}
/>

<SecurityCheck
title="Sequential Pattern"
status={result.has_sequential_pattern}
warning={true}
/>

<SecurityCheck
title="Keyboard Pattern"
status={result.has_keyboard_pattern}
warning={true}
/>

<SecurityCheck
title="Common Password"
status={result.is_common_password}
warning={true}
/>

</div>
        <h3>Suggestions</h3>

        <ul>
          {result.suggestions.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
    )}
  </motion.div>
);
}
export default PasswordAnalyzer;