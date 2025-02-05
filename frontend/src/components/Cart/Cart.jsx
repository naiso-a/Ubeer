import React, { useState } from 'react';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import '../../App.css';

const Cart = () => {
  const [cart, setCart] = useState(JSON.parse(localStorage.getItem('cart')) || []);

  const removeFromCart = (index) => {
    const updatedCart = cart.filter((_, i) => i !== index);
    setCart(updatedCart);
    localStorage.setItem('cart', JSON.stringify(updatedCart));
  };

  const clearCart = () => {
    setCart([]);
    localStorage.removeItem('cart');
  };

  return (
    <div className="cart-container">
      <h1>Votre Panier</h1>
      {cart.length === 0 ? (
        <Typography variant="h6">Votre panier est vide.</Typography>
      ) : (
        <Grid container spacing={3}>
          {cart.map((beer, index) => (
            <Grid item xs={12} sm={6} md={4} key={index}>
              <Card>
                <CardMedia
                  component="img"
                  height="140"
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
                    color="secondary"
                    onClick={() => removeFromCart(index)}
                    style={{ marginTop: '10px' }}
                  >
                    Retirer du panier
                  </Button>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}
      {cart.length > 0 && (
        <Button
          variant="contained"
          color="error"
          onClick={clearCart}
          style={{ marginTop: '20px' }}
        >
          Vider le panier
        </Button>
      )}
    </div>
  );
};

export default Cart;
