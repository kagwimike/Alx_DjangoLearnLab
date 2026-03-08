import { useState } from "react";
import API from "../api/api";

export default function CommentForm({ postId, parentId = null, onSuccess, initialText = "" }) {
  const [text, setText] = useState(initialText);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;

    setLoading(true);

    try {
      const res = await API.post("/api/comments/", {
        post: postId,
        content: text,
        parent: parentId, // for threaded replies
      });

      onSuccess(res.data); // update parent comment list
      setText("");
    } catch (err) {
      console.error(err);
      alert("Login required to comment or reply.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="comment-form">
      <textarea
        placeholder={parentId ? "Write a reply..." : "Write a comment..."}
        value={text}
        onChange={(e) => setText(e.target.value)}
        required
        disabled={loading}
      />
      <button type="submit" disabled={loading}>
        {loading ? "Posting..." : parentId ? "Reply" : "Post Comment"}
      </button>
    </form>
  );
}