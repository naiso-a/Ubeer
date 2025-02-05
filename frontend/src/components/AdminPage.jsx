import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Navigate } from "react-router-dom";

const AdminPage = () => {
  const { user, isAuthenticated, isLoading } = useAuth0();

  if (isLoading) return <p>Chargement...</p>;

  // Vérifier si l'utilisateur est connecté et a l'email admin
  if (!isAuthenticated || user?.email !== "admin@jesuisleadmin.com") {
    return <Navigate to="/" />;
  }

  return (
    <div>
      <h1>Bienvenue sur la page Admin</h1>
      <p>Seul l'administrateur peut voir cette page.</p>
    </div>
  );
};

export default AdminPage;
