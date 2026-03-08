import CommentItem from "./CommentItem";
import CommentForm from "./CommentForm";

export default function CommentList({ post }) {
  const handleAddComment = (newComment) => {
    post.comments.push(newComment);
  };

  const handleUpdateComment = (updatedComment) => {
    const idx = post.comments.findIndex(c => c.id === updatedComment.id);
    if (idx > -1) post.comments[idx] = updatedComment;
  };

  const handleDeleteComment = (commentId) => {
    post.comments = post.comments.filter(c => c.id !== commentId);
  };

  return (
    <div className="comments-section">
      <h2>Comments ({post.comments.length})</h2>

      <CommentForm postId={post.id} onSuccess={handleAddComment} />

      {post.comments.map((comment) => (
        <CommentItem
          key={comment.id}
          comment={comment}
          postId={post.id}
          onUpdateComment={handleUpdateComment}
          onDeleteComment={handleDeleteComment}
        />
      ))}
    </div>
  );
}