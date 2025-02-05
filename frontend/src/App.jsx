import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Auth0Provider } from "@auth0/auth0-react";
import { CartProvider } from "./components/Cart/CartContext";  // Vérifie bien le chemin !
import Home from "./components/Home";
import Navbar from "./components/Navbar";
import Brewery from "./components/Brewery/Brewery";
import Catalog from './components/Catalog/Catalog';
import AdminPage from "./components/AdminPage";
import Cart from "./components/Cart/Cart";
import AddBeerForm from './components/AddBeerForm';
import EditBeerForm from './components/EditBeerForm'
import AddBreweryForm from "./components/AddBrewery";
import EditBreweryForm from "./components/EditBreweryForm";

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
              <Route path='/Cart' element={<Cart />} />  {/* Ajout de la route pour le panier */}
              <Route path='/AdminPage' element={<AdminPage />} />
              <Route path="/admin/add-beer" element={<AddBeerForm />} />
              <Route path="/admin/edit-beer/:id" element={<EditBeerForm />} />
              <Route path="/admin/add-brewery" element={<AddBreweryForm/>} />
              <Route path="/admin/edit-brewery/:id" element={<EditBreweryForm />} />
            </Routes>
          </Router>
        </div>
      </CartProvider>
    </Auth0Provider>

  );
}

export default App;
