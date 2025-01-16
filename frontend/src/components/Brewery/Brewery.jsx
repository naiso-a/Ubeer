// Brewery.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import './Brewery.css'

const Brewery = ({ breweryName, beers, addToCart }) => {
  return (
    <div className="brewery-section">
      <h2>{breweryName}</h2>
      <div className="beer-list">
        {beers.map((beer) => (
          <div key={beer._id} className="beer-item">
            <img src={beer.image} alt={beer.name} className="beer-image" />
            <h3>{beer.name}</h3>
            <p>{beer.description}</p>
            <p>Prix : {beer.price}€</p>
            <button onClick={() => addToCart(beer)} className="add-to-cart-button">
              Ajouter au panier
            </button>
            <h1>test</h1>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Brewery;
