import { Link } from "react-router-dom";
import "../styles/PostCard.css";

function PostCard({ post }) {

  return (
    <Link 
      to={`/post/${post.id}`} 
      style={{ textDecoration: "none", color: "inherit" }}
    >

      <div className="post-card">

        <h2 className="post-title">{post.title}</h2>

        <p className="post-meta">
          By {post.author.username} | 
          {" "}
          {new Date(post.published_date).toLocaleDateString()}
        </p>

        <div className="tags-container">
          {post.tags.map(tag => (
            <span key={tag} className="tag">
              {tag}
            </span>
          ))}
        </div>

      </div>

    </Link>
  );
}

export default PostCard;