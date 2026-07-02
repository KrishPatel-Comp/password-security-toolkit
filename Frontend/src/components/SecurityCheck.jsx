import { FiCheckCircle, FiXCircle, FiAlertTriangle } from "react-icons/fi";
import "../styles/SecurityCheck.css";

function SecurityCheck({ title, status, warning = false }) {
  return (
    <div
      className={`security-check ${
        status ? (warning ? "warning" : "success") : "danger"
      }`}
    >
      {status ? (
        warning ? (
          <FiAlertTriangle />
        ) : (
          <FiCheckCircle />
        )
      ) : (
        <FiXCircle />
      )}

      <span>{title}</span>
    </div>
  );
}

export default SecurityCheck;