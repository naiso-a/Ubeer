import React from 'react';
import '../App.css';
import { useAuth0 } from "@auth0/auth0-react";
import LoginButton from "./LoginButton";  
import LogoutButton from "./Logout";  
import { Link } from 'react-router-dom';

const Navbar = () => {
  const { user, isAuthenticated } = useAuth0();

  return (
    <nav className="navbar">
      <h1 className="navbar-logo">
        <Link to="/" className="no-link-style">Ubeer</Link>
      </h1>
      <ul className="navbar-links">
      <li><a><Link to="/Catalog">Catalogue</Link></a></li>
      <li><a><Link to="/Brewery">Brasseries</Link></a></li>
        <li><a href="/Cart">Panier</a></li>
        <li>
          {isAuthenticated ? <LogoutButton /> : <LoginButton />}
        </li>
        {isAuthenticated && user?.email === "admin@jesuisleadmin.com" && (
          <li><Link to="/Admin">Admin</Link></li>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
