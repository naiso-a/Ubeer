// Home.jsx
import React, { useState } from 'react';
import Brewery from './Brewery/Brewery.jsx'; // Importer le composant Brewery
import '../App.css'; // Assurez-vous que le fichier CSS est lié correctement
import image from '../assets/images.jpg';
import Button from '@mui/material/Button';



const Home = () => {
  // Données simulées des bières
  const beers = [
    {
      _id: 1,
      name: 'Blonde de la Brasserie',
      brewery: 'Brasserie A',
      description: 'Une bière blonde légère et rafraîchissante.',
      price: 5.0,
      image: 'https://via.placeholder.com/150?text=Blonde'
    },
    {
      _id: 2,
      name: 'Rousse des Montagnes',
      brewery: 'Brasserie B',
      description: 'Une bière rousse avec des arômes de caramel.',
      price: 6.0,
      image: 'https://via.placeholder.com/150?text=Rousse'
    },
    {
      _id: 3,
      name: 'IPA Sauvage',
      brewery: 'Brasserie A',
      description: 'Une IPA avec un goût amer et une belle amertume.',
      price: 7.0,
      image: 'https://via.placeholder.com/150?text=IPA'
    },
    {
      _id: 4,
      name: 'Pale Ale Artisanale',
      brewery: 'Brasserie C',
      description: 'Une pale ale équilibrée avec des touches d’agrumes.',
      price: 6.5,
      image: 'https://via.placeholder.com/150?text=Pale+Ales'
    }
  ];

  // État du panier
  const [cart, setCart] = useState([]);

  // Fonction pour ajouter une bière au panier
  const addToCart = (beer) => {
    setCart([...cart, beer]);
  };

  // Groupement des bières par brasserie
  const groupBeersByBrewery = () => {
    return beers.reduce((acc, beer) => {
      if (!acc[beer.brewery]) {
        acc[beer.brewery] = [];
      }
      acc[beer.brewery].push(beer);
      return acc;
    }, {});
  };

  const groupedBeers = groupBeersByBrewery();

  return (
    <div className="home-container">
      <header className="home-header">
          <div className="text-with-stroke">
        <h1>Bienvenue sur Ubeer - Livraison de bière à domicile</h1>
        <p>Découvrez notre catalogue de bières, regroupées par brasserie, et ajoutez vos bières préférées au panier !</p>
      </div>
        <Button
          variant="contained"
          size="large"
          className="custom-button"
        >
          Voir toutes les bières
        </Button>
      </header>
    </div>
  );
};

export default Home;
