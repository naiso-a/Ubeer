import React, { createContext, useState } from "react";

// Création du contexte
export const CartContext = createContext();

// Fournisseur du contexte
export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState(JSON.parse(localStorage.getItem('cart')) || []);

  const addToCart = (beer) => {
    const updatedCart = [...cart, beer];
    setCart(updatedCart);
    localStorage.setItem('cart', JSON.stringify(updatedCart)); // Stocker dans localStorage
  };

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
    <CartContext.Provider value={{ cart, addToCart, removeFromCart, clearCart }}>
      {children}
    </CartContext.Provider>
  );
};
