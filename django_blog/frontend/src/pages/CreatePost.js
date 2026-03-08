// CreatePost.js
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/api";
import "../styles/createPost.css";

function CreatePost() {
  const navigate = useNavigate();
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [tags, setTags] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const tagArray = tags.split(",").map(tag => tag.trim());
      await API.post("/posts/", { title, content, tags: tagArray });
      navigate("/posts");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="editor-container">
      {/* Animated background blobs */}
      <div className="bg-blob"></div>
      <div className="bg-blob-2"></div>

      <div className="editor-card glass-effect animate-slide-up">
        <h1 className="text-overlay-effect">Create New Post</h1>
        <p className="subtitle">Share your thoughts with the world</p>

        <form onSubmit={handleSubmit} className="fade-in">
          <div className="input-group">
            <label>Title</label>
            <input
              type="text"
              placeholder="Give it a catchy title..."
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="title-input"
              required
            />
          </div>

          <div className="input-group">
            <label>Content</label>
            <textarea
              placeholder="What's on your mind?"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              className="content-editor"
              required
            />
          </div>

          <div className="input-group">
            <label>Tags</label>
            <input
              type="text"
              placeholder="e.g. python, django, react"
              value={tags}
              onChange={(e) => setTags(e.target.value)}
              className="tags-input"
            />
          </div>

          <button type="submit" className="publish-btn">
            <span>Publish Post</span>
          </button>
        </form>
      </div>
    </div>
  );
}

export default CreatePost;