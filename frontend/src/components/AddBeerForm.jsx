import React, { useState } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

const AddBeerForm = () => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [degree, setDegree] = useState('');
  const [idBrasserie, setIdBrasserie] = useState('');
  const [imageUrl, setImageUrl] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const newBeer = {
      name,
      description,
      price: parseFloat(price),
      degree: parseFloat(degree),
      id_brasserie: parseInt(idBrasserie),
      image_url: imageUrl,
    };

    try {
      await axios.post('http://127.0.0.1:5000/api/beers', newBeer);
      alert('Bière ajoutée avec succès');
    } catch (error) {
      console.error('Erreur lors de l\'ajout de la bière', error);
    }
  };

  return (
    <div>
      <h2>Ajouter une bière</h2>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Nom"
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
          label="Prix"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Degré"
          value={degree}
          onChange={(e) => setDegree(e.target.value)}
          fullWidth
          margin="normal"
        />
        <TextField
          label="ID Brasserie"
          value={idBrasserie}
          onChange={(e) => setIdBrasserie(e.target.value)}
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
          Ajouter la bière
        </Button>
      </form>
    </div>
  );
};

export default AddBeerForm;
