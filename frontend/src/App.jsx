import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Auth0Provider } from "@auth0/auth0-react";
import { CartProvider } from "./components/CartContext";  // Import du contexte
import Home from "./components/Home";
import Navbar from "./components/Navbar";
import Brewery from "./components/Brewery/Brewery";
import Catalog from './components/Catalog/Catalog';

function App() {
  return (
    <Auth0Provider
      domain="dev-r2ori0tgybwpisne.us.auth0.com" // Remplacez avec votre domaine Auth0
      clientId="7r6A6dS64vv7dk0rcUuZzmAOoVKyFmqt" // Remplacez avec votre clientId Auth0
      authorizationParams={{
        redirect_uri: window.location.origin, // Redirige vers l'URL actuelle après connexion
      }}
    >
    <CartProvider>  {/* Ajout du CartProvider ici */}
        <div className='App'>
          <Router>
            <Navbar />
            <Routes>
              <Route path='/' element={<Home />} />
              <Route path='/Catalog' element={<Catalog />} />
              <Route path='/Brewery' element={<Brewery />} />
            </Routes>
          </Router>
        </div>
      </CartProvider>
    </Auth0Provider>

  );
}

export default App;
