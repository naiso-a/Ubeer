import React, { useState } from 'react';
import Brewery from '../Brewery/Brewery.jsx'; // Vérifie le chemin
import '../../App.css'; // Vérifie le chemin vers App.css
import Button from '@mui/material/Button';

const Catalog = () => {
  const beers = [
    {
      _id: 1,
      name: 'Blonde de la Brasserie',
      brewery: 'Brasserie A',
      description: 'Une bière blonde légère et rafraîchissante.',
      price: 5.0,
      image: 'https://via.placeholder.com/150?text=Blonde'
    },
    // Autres bières...
  ];

  const [cart, setCart] = useState([]);

  const addToCart = (beer) => {
    setCart([...cart, beer]);
  };

  return (
    <div className="catalog-container">
      <h1>Bienvenue dans le Catalogue</h1>
      <Button
        href="Cart"
        variant="contained"
        size="large"
        className="custom-button"
      >
        Acheter
      </Button>
    </div>
  );
};

export default Catalog;
