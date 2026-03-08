import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import API from "../api/api";
import "../styles/login.css";

function Login() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await API.post("/token/", { username, password });
      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);
      navigate("/posts");
    } catch (err) {
      console.error(err);
      alert("Invalid username or password");
    }
  };

  return (
    <div className="auth-page">
      {/* Background Decor */}
      <div className="auth-orb orb-primary"></div>
      <div className="auth-orb orb-secondary"></div>

      <div className="auth-card glass-morphic animate-in">
        <div className="auth-header">
          <h2 className="text-gradient">Welcome Back</h2>
          <p className="auth-subtitle">Continue your developer journey</p>
        </div>

        <form onSubmit={handleLogin} className="auth-form">
          <div className="input-group">
            <input
              type="text"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>

          <div className="input-group password-wrapper">
            <input
              type={showPassword ? "text" : "password"}
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <span
              className="eye-toggle"
              onClick={() => setShowPassword(!showPassword)}
            >
              {showPassword ? "🙈" : "👁"}
            </span>
          </div>

          <button type="submit" className="login-btn">
            <span>Sign In</span>
          </button>
        </form>

        <div className="auth-footer">
          <p>New here? <Link to="/register">Create an account</Link></p>
        </div>
      </div>
    </div>
  );
}

export default Login;