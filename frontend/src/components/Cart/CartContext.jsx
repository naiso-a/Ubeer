import React, { createContext, useState } from "react";

// Création du contexte
export const CartContext = createContext();

// Fournisseur du contexte
export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState([]);

  // Fonction pour ajouter une bière au panier
  const addToCart = (beer) => {
    setCart([...cart, beer]);
  };

  return (
    <CartContext.Provider value={{ cart, addToCart }}>
      {children}
    </CartContext.Provider>
  );
};
