import "../styles/postDetails.css";

function CommentCard({ comment }) {

  return (
    <div className="comment-card">

      <div className="comment-header">
        <span className="comment-author">
          {comment.author.username}
        </span>

        <span className="comment-date">
          {new Date(comment.created_at).toLocaleDateString()}
        </span>
      </div>

      <p className="comment-content">
        {comment.content}
      </p>

    </div>
  );
}

export default CommentCard;