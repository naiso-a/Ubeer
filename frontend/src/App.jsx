import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Auth0Provider } from "@auth0/auth0-react";
import Home from "./components/Home";
import Navbar from "./components/Navbar";
import Brewery from "./components/Brewery/Brewery";

function App() {
  return (
    <Auth0Provider
      domain="dev-r2ori0tgybwpisne.us.auth0.com" // Remplacez avec votre domaine Auth0
      clientId="7r6A6dS64vv7dk0rcUuZzmAOoVKyFmqt" // Remplacez avec votre clientId Auth0
      authorizationParams={{
        redirect_uri: window.location.origin, // Redirige vers l'URL actuelle après connexion
      }}
    >
      <div className="App">
        <Router>
          <Navbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Brewery" element={<Brewery />} />
          </Routes>
        </Router>
      </div>
    </Auth0Provider>
  );
}

export default App;
