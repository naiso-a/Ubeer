import React, { useState } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

const AddBreweryForm = () => {
  const [name, setName] = useState('');
  const [location, setLocation] = useState('');
  const [breweryType, setBreweryType] = useState('');
  const [imageUrl, setImageUrl] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const newBrewery = {
      name,
      location,
      brewery_type: breweryType,
      image_url: imageUrl,
    };

    try {
      await axios.post('http://127.0.0.1:5000/api/breweries', newBrewery);
      alert('Brasserie ajoutée avec succès');
    } catch (error) {
      console.error('Erreur lors de l\'ajout de la brasserie', error);
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
          label="Emplacement"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Type de Brasserie"
          value={breweryType}
          onChange={(e) => setBreweryType(e.target.value)}
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
        <Button type="submit" variant="contained" color="primary" style={{ marginTop: '20px' }}>
          Ajouter la brasserie
        </Button>
      </form>
    </div>
  );
};

export default AddBreweryForm;
