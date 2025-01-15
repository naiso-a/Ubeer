import React from 'react';
import '../App.css';
import "./Brewery/Brewery";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1 className="navbar-logo">Ubeer</h1>
      <ul className="navbar-links">
        <li><a href="atalog">Catalogue</a></li>
        <li><a href="./Brewery/Brewery">Brasseries</a></li>
        <li><a href="#cart">Panier</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;
