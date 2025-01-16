import React from 'react';
import '../App.css';
import "./Brewery/Brewery";
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
    <h1 className="navbar-logo">
      <a href='../' className="no-link-style">Ubeer</a>
    </h1>
      <ul className="navbar-links">
        <li><a><Link to="/Catalog">Catalogue</Link></a></li>
        <li><a><Link to="/Brewery">Brasseries</Link></a></li>
        <li><a href="#cart">Panier</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;
