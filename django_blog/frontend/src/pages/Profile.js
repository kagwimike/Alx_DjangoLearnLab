import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import API from "../api/api";
import "../styles/profile.css";

function Profile() {
  const [profileData, setProfileData] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProfileData = async () => {
      try {
        // Ensure this matches your new Django path: api/profile/
        const res = await API.get("/profile/");
        setProfileData(res.data);
      } catch (err) {
        console.error("Error fetching profile:", err);
        // If the token is expired or invalid, redirect to login
        if (err.response?.status === 401) {
          navigate("/login");
        }
      } finally {
        setLoading(false);
      }
    };

    fetchProfileData();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.clear(); // Wipe tokens and username
    navigate("/login");
  };

  if (loading || !profileData) {
    return (
      <div className="profile-page-container">
        <div className="glass-panel animate-reveal">
          <div className="shimmer-wrapper">
            <p className="loading-text">Synchronizing data...</p>
            <div className="shimmer"></div>
          </div>
        </div>
      </div>
    );
  }

  const joinDate = profileData.date_joined 
    ? new Date(profileData.date_joined).toLocaleDateString('en-US', { month: 'short', year: 'numeric' })
    : "Member";

  return (
    <div className="profile-page-container">
      {/* Background Decor */}
      <div className="profile-orb profile-orb-1"></div>
      <div className="profile-orb profile-orb-2"></div>

      <div className="profile-content-wrapper">
        <div className="profile-card glass-panel animate-reveal">
          
          <div className="profile-header">
            <div className="avatar-container">
              <div className="avatar-image-placeholder">
                {(profileData.username || "U").charAt(0).toUpperCase()}
              </div>
              <div className="avatar-glow-overlay"></div>
            </div>

            <div className="profile-titles">
              <h1 className="hero-text-gradient">
                User <span className="text-overlay-effect">Profile</span>
              </h1>
              <p className="welcome-text animate-text-pop">
                Welcome back, <span className="username-highlight">@{profileData.username}</span>!
              </p>
            </div>

            <button className="logout-glass-btn" onClick={handleLogout}>
              Logout
            </button>
          </div>

          <div className="profile-divider"></div>

          <div className="profile-grid">
            <div className="grid-item glass-panel-sm">
              <span className="stat-label">Posts Published</span>
              <span className="stat-value">{profileData.post_count || 0}</span>
            </div>
            <div className="grid-item glass-panel-sm">
              <span className="stat-label">Total Comments</span>
              <span className="stat-value">{profileData.comment_count || 0}</span>
            </div>
            <div className="grid-item glass-panel-sm">
              <span className="stat-label">Member Since</span>
              <span className="stat-value">{joinDate}</span>
            </div>
          </div>
          
          {/* Subtle footer text overlay */}
          <div className="profile-footer-overlay">
            DEV_CREDENTIALS_SECURE
          </div>
        </div>
      </div>
    </div>
  );
}

export default Profile;