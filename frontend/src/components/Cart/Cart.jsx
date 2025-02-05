import React, { useContext, useState } from 'react';
import { CartContext } from './CartContext'; // Vérifie l'import
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import Modal from '@mui/material/Modal';
import Box from '@mui/material/Box';

const Cart = () => {
  const { cart, removeFromCart, clearCart } = useContext(CartContext);
  const [open, setOpen] = useState(false);

  const handlePurchase = () => {
    setOpen(true); // Ouvre la popup
    setTimeout(() => {
      setOpen(false);
      clearCart(); // Vide le panier après 2 secondes
    }, 2000);
  };

  return (
    <div className="cart-container" style={{ textAlign: 'center', padding: '20px' }}>
      <h1>Votre Panier</h1>
      {cart.length === 0 ? (
        <Typography variant="h6">Votre panier est vide.</Typography>
      ) : (
        <Grid container spacing={3} justifyContent="center">
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
                  <Typography variant="body2">{beer.description}</Typography>
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

      {/* Boutons "Acheter" et "Vider le panier" (centrés) */}
      {cart.length > 0 && (
        <div style={{ 
          display: 'flex', 
          justifyContent: 'center', 
          gap: '20px', 
          marginTop: '20px' 
        }}>
          <Button variant="contained" color="success" onClick={handlePurchase}>
            Acheter
          </Button>
          <Button variant="contained" color="error" onClick={clearCart}>
            Vider le panier
          </Button>
        </div>
      )}

      {/* Popup d'achat */}
      <Modal open={open} onClose={() => setOpen(false)}>
        <Box
          sx={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            bgcolor: 'white',
            boxShadow: 24,
            p: 4,
            borderRadius: 2,
            textAlign: 'center',
          }}
        >
          <Typography variant="h6">🍻 Bière bien achetée !</Typography>
        </Box>
      </Modal>
    </div>
  );
};

export default Cart;
