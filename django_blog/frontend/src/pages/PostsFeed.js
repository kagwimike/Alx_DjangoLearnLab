import { useEffect, useState } from "react";
import API from "../api/api";
import PostCard from "../components/PostCard";
import "../styles/postsFeed.css";

function PostsFeed() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const res = await API.get("/posts/");
        setPosts(res.data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };
    fetchPosts();
  }, []);

  return (
    <div className="feed-page">
      {/* Dynamic Ambient Background */}
      <div className="ambient-light light-blue"></div>
      <div className="ambient-light light-purple"></div>

      <div className="feed-container">
        <header className="feed-header animate-slide-down">
          <h1 className="feed-title-text text-overlay-gradient">Latest Insights</h1>
          <p className="feed-subtitle">Explore the newest technical discussions from the community.</p>
        </header>

        {loading ? (
          <div className="loading-grid">
            {[1, 2, 3, 4].map((n) => (
              <div key={n} className="skeleton-card glass-morphic"></div>
            ))}
          </div>
        ) : (
          <div className="posts-grid">
            {posts.length === 0 ? (
              <div className="empty-state glass-morphic animate-fade-in">
                <h3>No posts found</h3>
                <p>The community is quiet... for now.</p>
              </div>
            ) : (
              posts.map((post, index) => (
                <div 
                  className="post-card-wrapper animate-staggered" 
                  style={{ "--index": index }} 
                  key={post.id}
                >
                  <PostCard post={post} />
                </div>
              ))
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default PostsFeed;