import { useEffect, useState, useCallback } from "react";
import { useParams, useNavigate } from "react-router-dom";
import API from "../api/api";
import "../styles/postDetails.css";

function PostDetails() {
  const { id } = useParams();
  const navigate = useNavigate();
  
  // State
  const [post, setPost] = useState(null);
  const [comments, setComments] = useState([]);
  const [commentText, setCommentText] = useState("");
  const [editingCommentId, setEditingCommentId] = useState(null);
  const [editedText, setEditedText] = useState("");
  const [replyText, setReplyText] = useState({});
  const [replyingToId, setReplyingToId] = useState(null);

  // 1. Memoized Fetch Function (Fixes ESLint warning)
  const fetchPost = useCallback(async () => {
    try {
      const res = await API.get(`posts/${id}/`);
      setPost(res.data);
      setComments(res.data.comments || []);
    } catch (err) {
      console.error("Failed to fetch post:", err);
    }
  }, [id]);

  useEffect(() => {
    fetchPost();
  }, [fetchPost]);

  // --- Post Management Handlers ---
  const handleDeletePost = async () => {
    if (!window.confirm("Are you sure you want to delete this post?")) return;
    try {
      await API.delete(`posts/${id}/`);
      navigate("/"); // Redirect to feed after deletion
    } catch (err) {
      alert("Error deleting post. You may not have permission.");
    }
  };

  const handleEditPost = () => {
    navigate(`/posts/${id}/edit`); // Adjust path based on your App.js routing
  };

  // --- Comment Handlers ---
  const handleCommentSubmit = async (e, parentId = null) => {
    e.preventDefault();
    const content = parentId ? replyText[parentId] : commentText;
    if (!content?.trim()) return;

    try {
      const res = await API.post("comments/", {
        post: id,
        content,
        parent: parentId,
      });

      if (parentId) {
        setComments(updateNestedReplies(comments, parentId, res.data));
        setReplyText({ ...replyText, [parentId]: "" });
        setReplyingToId(null);
      } else {
        setComments([...comments, res.data]);
        setCommentText("");
      }
    } catch (err) {
      alert("Please login to participate in the discussion.");
    }
  };

  const handleUpvote = async (commentId) => {
    try {
      const response = await API.post(`comments/${commentId}/upvote/`);
      setComments(updateCommentInList(comments, commentId, response.data.upvotes));
    } catch (err) {
      if (err.response?.status === 400) alert(err.response.data.error);
    }
  };

  const handleDeleteComment = async (commentId) => {
    if (!window.confirm("Delete this comment?")) return;
    try {
      await API.delete(`comments/${commentId}/`);
      setComments(removeComment(comments, commentId));
    } catch (err) {
      console.error(err);
    }
  };

  const handleEditComment = async (commentId) => {
    try {
      const res = await API.patch(`comments/${commentId}/`, { content: editedText });
      setComments(replaceComment(comments, res.data));
      setEditingCommentId(null);
    } catch (err) {
      console.error(err);
    }
  };

  // --- Recursive Helpers (Keep as is) ---
  const updateNestedReplies = (list, parentId, newReply) =>
    list.map((c) => {
      if (c.id === parentId) return { ...c, replies: [...(c.replies || []), newReply] };
      if (c.replies?.length) return { ...c, replies: updateNestedReplies(c.replies, parentId, newReply) };
      return c;
    });

  const updateCommentInList = (list, id, newCount) =>
    list.map((c) => {
      if (c.id === id) return { ...c, upvotes: newCount };
      if (c.replies?.length) return { ...c, replies: updateCommentInList(c.replies, id, newCount) };
      return c;
    });

  const replaceComment = (list, updated) =>
    list.map((c) => {
      if (c.id === updated.id) return { ...updated, replies: c.replies };
      if (c.replies?.length) return { ...c, replies: replaceComment(c.replies, updated) };
      return c;
    });

  const removeComment = (list, idToRemove) =>
    list
      .filter((c) => c.id !== idToRemove)
      .map((c) => ({
        ...c,
        replies: c.replies ? removeComment(c.replies, idToRemove) : [],
      }));

  // --- Recursive Component Render ---
  const renderComments = (commentsList, depth = 0) =>
    commentsList.map((comment) => (
      <div key={comment.id} className={`comment-thread ${depth > 0 ? 'nested' : ''}`} style={{ '--depth': depth }}>
        <div className="comment-card glass-panel-sm">
          <div className="comment-header">
            <span className="comment-author">@{comment.author.username}</span>
            <div className="upvote-badge" onClick={() => handleUpvote(comment.id)}>
              <span className="arrow">▲</span>
              <span className="count">{comment.upvotes || 0}</span>
            </div>
          </div>

          {editingCommentId === comment.id ? (
            <div className="edit-area">
              <textarea
                className="edit-textarea"
                value={editedText}
                onChange={(e) => setEditedText(e.target.value)}
              />
              <div className="action-row">
                <button className="btn-save" onClick={() => handleEditComment(comment.id)}>Update</button>
                <button className="btn-cancel" onClick={() => setEditingCommentId(null)}>Cancel</button>
              </div>
            </div>
          ) : (
            <>
              <p className="comment-body">{comment.content}</p>
              <div className="comment-actions">
                <button className="action-link" onClick={() => setReplyingToId(comment.id)}>Reply</button>
                <button className="action-link" onClick={() => { setEditingCommentId(comment.id); setEditedText(comment.content); }}>Edit</button>
                <button className="action-link delete" onClick={() => handleDeleteComment(comment.id)}>Delete</button>
              </div>
            </>
          )}

          {replyingToId === comment.id && (
            <form onSubmit={(e) => handleCommentSubmit(e, comment.id)} className="reply-form animate-fade-in">
              <textarea
                placeholder="Write your reply..."
                value={replyText[comment.id] || ""}
                onChange={(e) => setReplyText({ ...replyText, [comment.id]: e.target.value })}
                required
              />
              <div className="action-row">
                <button type="submit" className="btn-reply">Post Reply</button>
                <button type="button" className="btn-cancel" onClick={() => setReplyingToId(null)}>Cancel</button>
              </div>
            </form>
          )}
        </div>
        {comment.replies?.length > 0 && renderComments(comment.replies, depth + 1)}
      </div>
    ));

  if (!post) return <div className="loading-screen"><div className="spinner"></div></div>;

  return (
    <div className="post-details-page">
      <div className="orb post-orb-1"></div>
      <div className="orb post-orb-2"></div>

      <div className="post-details-container">
        <article className="post-card glass-card animate-slide-up">
          <header className="post-header">
            {/* Admin Actions for Post */}
            <div className="post-admin-actions">
              <button className="action-btn edit" onClick={handleEditPost}>Edit Post</button>
              <button className="action-btn delete" onClick={handleDeletePost}>Delete Post</button>
            </div>
            
            <h1 className="post-title text-gradient">{post.title}</h1>
            <div className="post-meta">
              <span className="author-badge">@{post.author.username}</span>
              <span className="dot">•</span>
              <time>{new Date(post.published_date).toLocaleDateString(undefined, { dateStyle: 'long' })}</time>
            </div>
            <div className="post-tags">
              {post.tags.map((tag) => <span key={tag} className="tag-chip">{tag}</span>)}
            </div>
          </header>

          <div className="post-content-body">{post.content}</div>
        </article>

        <section className="comments-section animate-fade-in">
          <div className="section-header">
            <h2 className="section-title">Discussion</h2>
            <span className="comment-count-badge">{comments.length} Comments</span>
          </div>

          <div className="comment-list">
            {comments.length === 0 ? (
              <div className="no-comments-placeholder glass-panel-sm">
                <p>No comments yet. Start the conversation!</p>
              </div>
            ) : renderComments(comments)}
          </div>

          <div className="main-comment-form glass-card">
            <h3>Share your thoughts</h3>
            <form onSubmit={(e) => handleCommentSubmit(e)}>
              <textarea
                placeholder="What are your thoughts on this?"
                value={commentText}
                onChange={(e) => setCommentText(e.target.value)}
                required
              />
              <button type="submit" className="glow-button">Post Comment</button>
            </form>
          </div>
        </section>
      </div>
    </div>
  );
}

export default PostDetails;