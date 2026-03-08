import { Navigate, useLocation } from "react-router-dom";

function PrivateRoute({ children }) {

  const location = useLocation();
  const token = localStorage.getItem("access");

  if (!token) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}

export default PrivateRoute;