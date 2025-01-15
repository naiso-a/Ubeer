// Home.jsx
import React, { useState } from 'react';
import Brewery from './Brewery/Brewery.jsx'; // Importer le composant Brewery
import '../App.css'; // Assurez-vous que le fichier CSS est lié correctement

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
        <h1>Bienvenue sur Ubeer - Livraison de bière à domicile</h1>
        <h1>Je suis un connard</h1>
        <p>Découvrez notre catalogue de bières, regroupées par brasserie, et ajoutez vos bières préférées au panier !</p>
      </header>

      {/* Liste des bières groupées par brasserie */}
      <section className="beer-catalog">
        {Object.keys(groupedBeers).map((brewery) => (
          <Brewery 
            key={brewery} 
            breweryName={brewery} 
            beers={groupedBeers[brewery]} 
            addToCart={addToCart}
          />
        ))}
      </section>

      {/* Section panier */}
      <section className="cart-section">
        <h2>Mon Panier</h2>
        {cart.length === 0 ? (
          <p>Votre panier est vide. Ajoutez des bières pour commencer.</p>
        ) : (
          <ul>
            {cart.map((beer, index) => (
              <li key={index}>
                {beer.name} - {beer.price}€
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  );
};

export default Home;
