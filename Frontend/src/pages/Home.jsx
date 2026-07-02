import PasswordAnalyzer from "../components/PasswordAnalyzer";
import "../styles/Home.css";
import AnimatedBackground from "../components/AnimatedBackground";

<>
  <AnimatedBackground />

  <div className="home">
    ...
  </div>
</>

function Home() {
  return (
    <div className="home">
      <div className="container">
        <h1>Password Security Toolkit</h1>
        <p className="subtitle">
          Analyze password strength, entropy, crack time, and security patterns.
        </p>

        <PasswordAnalyzer />
      </div>
    </div>
  );
}

export default Home;