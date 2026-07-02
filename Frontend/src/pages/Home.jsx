import PasswordAnalyzer from "../components/PasswordAnalyzer";
import AnimatedBackground from "../components/AnimatedBackground";
import "../styles/Home.css";

function Home() {
  return (
    <>
      <AnimatedBackground />

      <div className="home">
        <div className="container">
          <h1>Password Security Toolkit</h1>

          <p className="subtitle">
            Analyze passwords with entropy calculation, pattern detection, and
            real-time security scoring.
          </p>

          <div className="feature-tags">
            <span>Entropy</span>
            <span>Pattern Detection</span>
            <span>Live Analysis</span>
            <span>FastAPI</span>
            <span>React</span>
          </div>

          <PasswordAnalyzer />
        </div>
      </div>
    </>
  );
}

export default Home;