import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import '../../App.css';


const Catalog = () => {
  const [beers, setBeers] = useState([]);
  const [cart, setCart] = useState(JSON.parse(localStorage.getItem('cart')) || []);

  // Récupération des bières depuis l'API
  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL;

    axios.get(`${apiUrl}/api/beers`)
      .then(response => setBeers(response.data))
      .catch(error => console.error('Erreur lors de la récupération des bières:', error));
  }, []);

  // Ajouter une bière au panier et sauvegarder dans localStorage
  const addToCart = (beer) => {
    const updatedCart = [...cart, beer];
    setCart(updatedCart);
    localStorage.setItem('cart', JSON.stringify(updatedCart)); // Sauvegarde
  };

  return (
    <div className="catalog-container">
      <h1>Bienvenue dans le Catalogue</h1>
      <Grid container spacing={3}>
        {beers.map(beer => (
          <Grid item xs={12} sm={6} md={4} key={beer.id}>
            <Card>
                <CardMedia
                    component="img"
                    className="beer-image"
                    image={beer.image_url || 'https://via.placeholder.com/150?text=Biere'}
                    alt={beer.name}
                />
              <CardContent>
                <Typography variant="h6">{beer.name}</Typography>
                <Typography variant="body2" color="textSecondary">
                  {beer.description}
                </Typography>
                <Typography variant="body1">Prix: {beer.price}€</Typography>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={() => addToCart(beer)}
                  style={{ marginTop: '10px' }}
                >
                  Ajouter au panier
                </Button>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
      <Button
        href="/Cart"
        variant="contained"
        size="large"
        className="custom-button"
        style={{ marginTop: '20px' }}
      >
        Voir le Panier ({cart.length})
      </Button>
    </div>
  );
};

export default Catalog;
