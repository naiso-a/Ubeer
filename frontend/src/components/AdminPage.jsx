import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

const AdminPage = () => {
  const [beers, setBeers] = useState([]);
  const [brasseries, setBrasseries] = useState([]);

  // Récupération des bières et des brasseries
  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL;
    axios.get(`${apiUrl}/api/beers`)
      .then(response => setBeers(response.data))
      .catch(error => console.error('Erreur lors de la récupération des bières', error));

    axios.get(`${apiUrl}/api/brasseries`)
      .then(response => setBrasseries(response.data))
      .catch(error => console.error('Erreur lors de la récupération des brasseries', error));
  }, []);

  const deleteBeer = (id) => {
    const apiUrl = process.env.REACT_APP_API_URL;

    axios.delete(`${apiUrl}/api/beers/${id}`)
      .then(() => {
        setBeers(beers.filter(beer => beer.id !== id));  // Mettre à jour l'état des bières
        alert('Bière supprimée avec succès');
      })
      .catch(error => {
        console.error('Erreur lors de la suppression de la bière', error);
        alert('Une erreur est survenue lors de la suppression de la bière');
      });
  };

  // Supprimer une brasserie
  const deleteBrewery = (id) => {
    const apiUrl = process.env.REACT_APP_API_URL;
    axios.delete(`${apiUrl}/api/brasseries/${id}`)
      .then(() => {
        setBrasseries(brasseries.filter(brewery => brewery.id !== id));  // Supprimer la brasserie de l'état
        alert('Brasserie supprimée avec succès');
      })
      .catch(error => console.error('Erreur lors de la suppression de la brasserie', error));
  };

  return (
    <div>
      <h1>Page d'Administration</h1>

      {/* Bières */}
      <div>
        <h2>Liste des Bières</h2>
        <Grid container spacing={3}>
          {beers.map((beer) => (
            <Grid item xs={12} sm={6} md={4} key={beer.id}>
              <Card>
                <CardMedia
                  component="img"
                  height="140"
                  image={beer.image_url || 'https://via.placeholder.com/150?text=Biere'}
                  alt={beer.name}
                />
                <CardContent>
                  <Typography variant="h6">{beer.name}</Typography>
                  <Typography variant="body2" color="textSecondary">{beer.description}</Typography>
                  <Typography variant="body1">Degré: {beer.degree}%</Typography>
                  <Typography variant="body1">Prix: {beer.price}€</Typography>
                  <Button
                    variant="contained"
                    color="primary"
                    href={`/admin/edit-beer/${beer.id}`}
                    style={{ marginTop: '10px', marginRight: '10px' }}
                  >
                    Modifier
                  </Button>
                  <Button
                    variant="contained"
                    color="secondary"
                    onClick={() => deleteBeer(beer.id)}
                    style={{ marginTop: '10px' }}
                  >
                    Supprimer
                  </Button>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </div>

      {/* Brasseries */}
      <div>
        <h2>Liste des Brasseries</h2>
        <Grid container spacing={3}>
          {brasseries.map((brewery) => (
            <Grid item xs={12} sm={6} md={4} key={brewery.id}>
              <Card>
                <CardMedia
                  component="img"
                  height="140"
                  image={brewery.image_url || 'https://via.placeholder.com/150?text=Brasserie'}
                  alt={brewery.name}
                />
                <CardContent>
                  <Typography variant="h6">{brewery.name}</Typography>
                  <Typography variant="body2" color="textSecondary">{brewery.description}</Typography>
                  <Button
                    variant="contained"
                    color="primary"
                    href={`/admin/edit-brewery/${brewery.id}`}
                    style={{ marginTop: '10px', marginRight: '10px' }}
                  >
                    Modifier
                  </Button>
                  <Button
                    variant="contained"
                    color="secondary"
                    onClick={() => deleteBrewery(brewery.id)}
                    style={{ marginTop: '10px' }}
                  >
                    Supprimer
                  </Button>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </div>

      {/* Bouton pour ajouter une bière */}
      <Button
        variant="contained"
        color="primary"
        href="/admin/add-beer"
        style={{ marginTop: '20px' }}
      >
        Ajouter une Bière
      </Button>

      {/* Bouton pour ajouter une brasserie */}
      <Button
        variant="contained"
        color="primary"
        href="/admin/add-brewery"
        style={{ marginTop: '20px', marginLeft: '10px' }}
      >
        Ajouter une Brasserie
      </Button>
    </div>
  );
};

export default AdminPage;
