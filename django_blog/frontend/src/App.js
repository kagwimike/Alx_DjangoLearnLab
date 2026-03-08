import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Footer from './components/Footer';

import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import PostsFeed from "./pages/PostsFeed";
import CreatePost from "./pages/CreatePost";
import PostDetails from "./pages/PostDetails";
import Profile from "./pages/Profile";

import "./App.css"; // Ensure you have layout CSS here

function App() {
  return (
    <Router>
      <div className="app-layout">
        <Navbar />

        {/* The 'main' tag acts as the flexible middle section */}
        <main className="main-content">
          <div className="container">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/posts" element={<PostsFeed />} />
              <Route path="/create" element={<CreatePost />} />
              <Route path="/post/:id" element={<PostDetails />} />
              <Route path="/profile" element={<Profile />} />
            </Routes>
          </div>
        </main>

        <Footer />
      </div>
    </Router>
  );
}

export default App;