import React from 'react';
import '../App.css';
import { useAuth0 } from "@auth0/auth0-react";
import LoginButton from "./LoginButton";  // Assurez-vous que le fichier LoginButton.jsx existe
import LogoutButton from "./Logout";  // Assurez-vous que le fichier LogoutButton.jsx existe

const Navbar = () => {
  const { isAuthenticated } = useAuth0(); // Utilise le hook useAuth0 pour vérifier l'état de l'authentification

  return (
    <nav className="navbar">
      <h1 className="navbar-logo">Ubeer</h1>
      <ul className="navbar-links">
        <li><a href="/">Catalogue</a></li>
        <li><a href="./Brewery/Brewery">Brasseries</a></li>
        <li><a href="#cart">Panier</a></li>
        <li>
          {/* Si l'utilisateur est connecté, affiche le bouton de déconnexion, sinon le bouton de connexion */}
          {isAuthenticated ? <LogoutButton /> : <LoginButton />}
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
