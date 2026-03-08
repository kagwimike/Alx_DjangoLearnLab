import React from 'react';
import { Link } from 'react-router-dom';
import "../styles/home.css";

function Home() {
  const features = [
    {
      title: "Real-time Engagement",
      description: "Upvote, comment, and interact with fellow developers instantly.",
      icon: "🚀"
    },
    {
      title: "Secure Auth",
      description: "Enterprise-grade security using JWT and Django Rest Framework.",
      icon: "🔐"
    },
    {
      title: "Threaded Discussions",
      description: "Deep-nested comments for organized and meaningful technical debates.",
      icon: "💬"
    }
  ];

  return (
    <div className="home-container">
      {/* Background Orbs */}
      <div className="orb orb-1"></div>
      <div className="orb orb-2"></div>

      <div className="home-content">
        {/* Hero Section */}
        <div className="home-card glass-panel animate-reveal">
          <div className="badge">New Features Available</div>
          <h1 className="hero-text-gradient">
            Welcome to <span className="text-glow">DevBlog</span>
          </h1>
          <p className="description">
            The ultimate ecosystem for modern Bloggers.
          </p>
          <div className="cta-group">
            <Link to="/posts" className="btn-primary">Get Started</Link>
          </div>
        </div>

        {/* Feature Grid */}
        <div className="features-grid">
          {features.map((f, index) => (
            <div key={index} className="feature-card glass-panel-sm animate-fade-in" style={{animationDelay: `${index * 0.2}s`}}>
              <div className="feature-icon">{f.icon}</div>
              <h3>{f.title}</h3>
              <p>{f.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Home;