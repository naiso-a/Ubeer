import React from 'react';
import '../App.css';
import { useAuth0 } from "@auth0/auth0-react";
import LoginButton from "./LoginButton";  // Assurez-vous que le fichier LoginButton.jsx existe
import LogoutButton from "./Logout";  //
import { Link } from 'react-router-dom';

const Navbar = () => {
  const { isAuthenticated } = useAuth0(); // Utilise le hook useAuth0 pour vérifier l'état de l'authentification

  return (
    <nav className="navbar">
    <h1 className="navbar-logo">
      <a href='../' className="no-link-style">Ubeer</a>
    </h1>
      <ul className="navbar-links">
      <li><a><Link to="/Catalog">Catalogue</Link></a></li>
      <li><a><Link to="/Brewery">Brasseries</Link></a></li>
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
