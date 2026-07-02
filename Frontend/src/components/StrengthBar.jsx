import "../styles/StrengthBar.css";

function StrengthBar({ score }) {
  let color = "#ef4444";

  if (score >= 80) {
    color = "#22c55e";
  } else if (score >= 60) {
    color = "#3b82f6";
  } else if (score >= 40) {
    color = "#f59e0b";
  }

  return (
    <div className="strength-container">
      <div
        className="strength-fill"
        style={{
          width: `${score}%`,
          backgroundColor: color,
        }}
      />
    </div>
  );
}

export default StrengthBar;