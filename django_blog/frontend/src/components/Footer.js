// src/components/Footer.js
import React from 'react';
import { Link } from 'react-router-dom';
import "../styles/footer.css";

function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="glass-footer">
      <div className="footer-content">
        <div className="footer-section brand">
          <h2 className="footer-logo">
            Dev<span className="text-overlay-effect">Blog</span>
          </h2>
          <p className="footer-tagline">Building the future, one byte at a time.</p>
          
          {/* Social Icons Integrated in Brand Section */}
          <div className="social-links-container">
            <a href="https://linkedin.com" target="_blank" rel="noreferrer" className="social-icon">
              <i className="fa-brands fa-linkedin-in"></i>
            </a>
            <a href="https://twitter.com" target="_blank" rel="noreferrer" className="social-icon">
              <i className="fa-brands fa-x-twitter"></i>
            </a>
            <a href="https://facebook.com" target="_blank" rel="noreferrer" className="social-icon">
              <i className="fa-brands fa-facebook-f"></i>
            </a>
            <a href="https://github.com" target="_blank" rel="noreferrer" className="social-icon">
              <i className="fa-brands fa-github"></i>
            </a>
          </div>
        </div>

        <div className="footer-section links">
          <h4>Navigation</h4>
          <div className="link-grid">
            <Link to="/">Home</Link>
            <Link to="/posts">Explore</Link>
            <Link to="/profile">Profile</Link>
            <Link to="/search">Search</Link>
          </div>
        </div>

        <div className="footer-section status">
          <h4>System Status</h4>
          <div className="status-indicator">
            <span className="pulse-dot"></span>
            <span className="status-text">API Online</span>
          </div>
          <p className="version-text">v2.4.0-stable</p>
        </div>
      </div>

      <div className="footer-bottom">
        <div className="footer-divider"></div>
        <div className="footer-copy">
          <span>&copy; {currentYear} DjangoLearnLab. All rights reserved.</span>
          <span className="made-with">Made with <i className="fa-solid fa-heart heart-pulse"></i> for Developers</span>
        </div>
      </div>
    </footer>
  );
}

export default Footer;