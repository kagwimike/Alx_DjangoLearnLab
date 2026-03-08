import { useState } from "react";
import API from "../api/api";
import CommentForm from "./CommentForm";

export default function CommentItem({ comment, postId, onUpdateComment, onDeleteComment }) {
  const [editing, setEditing] = useState(false);
  const [showReply, setShowReply] = useState(false);
  const [editedText, setEditedText] = useState(comment.content);

  const handleSaveEdit = async () => {
    try {
      const res = await API.patch(`/api/comments/${comment.id}/`, {
        content: editedText,
      });
      onUpdateComment(res.data);
      setEditing(false);
    } catch (err) {
      console.error(err);
    }
  };

  const handleDelete = async () => {
    if (!confirm("Are you sure you want to delete this comment?")) return;
    try {
      await API.delete(`/api/comments/${comment.id}/`);
      onDeleteComment(comment.id);
    } catch (err) {
      console.error(err);
    }
  };

  const handleUpvote = async () => {
    try {
      const res = await API.post(`/api/comments/${comment.id}/upvote/`);
      onUpdateComment(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="comment-item">
      <div className="comment-header">
        <strong>{comment.author.username}</strong> •{" "}
        {new Date(comment.created_at).toLocaleString()}
      </div>

      {editing ? (
        <>
          <textarea
            value={editedText}
            onChange={(e) => setEditedText(e.target.value)}
          />
          <div className="comment-actions">
            <button onClick={handleSaveEdit}>Save</button>
            <button onClick={() => setEditing(false)}>Cancel</button>
          </div>
        </>
      ) : (
        <>
          <p>{comment.content}</p>
          <div className="comment-actions">
            <button onClick={handleUpvote}>▲ {comment.upvotes || 0}</button>
            {comment.is_author && <button onClick={() => setEditing(true)}>Edit</button>}
            {comment.is_author && <button onClick={handleDelete}>Delete</button>}
            <button onClick={() => setShowReply(!showReply)}>Reply</button>
          </div>
        </>
      )}

      {showReply && (
        <CommentForm
          postId={postId}
          parentId={comment.id}
          onSuccess={(reply) => {
            if (!comment.replies) comment.replies = [];
            comment.replies.push(reply);
            onUpdateComment(comment);
            setShowReply(false);
          }}
        />
      )}

      {comment.replies && comment.replies.length > 0 && (
        <div className="replies">
          {comment.replies.map((reply) => (
            <CommentItem
              key={reply.id}
              comment={reply}
              postId={postId}
              onUpdateComment={(updatedReply) => {
                const idx = comment.replies.findIndex(r => r.id === updatedReply.id);
                comment.replies[idx] = updatedReply;
                onUpdateComment(comment);
              }}
              onDeleteComment={(replyId) => {
                comment.replies = comment.replies.filter(r => r.id !== replyId);
                onUpdateComment(comment);
              }}
            />
          ))}
        </div>
      )}
    </div>
  );
}