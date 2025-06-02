import React, { useState } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

const AddBreweryForm = () => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [latitude, setLatitude] = useState('');
  const [longitude, setLongitude] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const apiUrl = process.env.REACT_APP_API_URL;

    const newBrewery = {
      name,
      description,
      image_url: imageUrl,
      latitude: parseFloat(latitude),   // conversion en nombre
      longitude: parseFloat(longitude), // conversion en nombre
    };

    try {
      await axios.post(`${apiUrl}/api/brasseries`, newBrewery);
      alert('Brasserie ajoutée avec succès');
    } catch (error) {
      console.error("Erreur lors de l'ajout de la brasserie", error);
    }
  };

  return (
      <div>
        <h2>Ajouter une brasserie</h2>
        <form onSubmit={handleSubmit}>
          <TextField
              label="Nom de la Brasserie"
              value={name}
              onChange={(e) => setName(e.target.value)}
              fullWidth
              margin="normal"
          />
          <TextField
              label="Description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              fullWidth
              margin="normal"
          />
          <TextField
              label="URL de l'image"
              value={imageUrl}
              onChange={(e) => setImageUrl(e.target.value)}
              fullWidth
              margin="normal"
          />
          <TextField
              label="Latitude"
              value={latitude}
              onChange={(e) => setLatitude(e.target.value)}
              fullWidth
              margin="normal"
          />
          <TextField
              label="Longitude"
              value={longitude}
              onChange={(e) => setLongitude(e.target.value)}
              fullWidth
              margin="normal"
          />
          <Button
              type="submit"
              variant="contained"
              color="primary"
              style={{ marginTop: '20px' }}
          >
            Ajouter la brasserie
          </Button>
        </form>
      </div>
  );
};

export default AddBreweryForm;
