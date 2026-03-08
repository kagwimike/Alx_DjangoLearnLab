import { Link, useNavigate } from "react-router-dom";
import "../styles/navbar.css";

function Navbar(){

  const navigate = useNavigate();

  const token = localStorage.getItem("access"); // ✅ fixed

  const handleLogout = () => {

    localStorage.removeItem("access");
    localStorage.removeItem("refresh");

    navigate("/login");

  };

  return(

    <nav className="navbar">

      <div className="nav-container">

        <h2 className="logo" onClick={()=>navigate("/")}>
          DevBlog
        </h2>

        <div className="nav-links">

          <Link to="/">Home</Link>

          <Link to="/posts">Posts</Link>

          {!token && (
            <>
              <Link className="login-link" to="/login">Login</Link>
              <Link className="register-link" to="/register">Register</Link>
            </>
          )}

          {token && (
            <>
              <Link to="/create">Create Post</Link>
              <Link to="/profile">Profile</Link>

              <button
                onClick={handleLogout}
                className="logout-btn"
              >
                Logout
              </button>
            </>
          )}

        </div>

      </div>

    </nav>

  );

}

export default Navbar;