import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

const EditBeerForm = () => {
  const { id } = useParams();
  const [beer, setBeer] = useState(null);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL;
    axios.get(`${apiUrl}/api/beers/${id}`)
      .then(response => {
        setBeer(response.data);
      })
      .catch(error => {
        console.error('Erreur lors de la récupération de la bière:', error);
      });
  }, [id]);

  const handleSubmit = async (e) => {
    const apiUrl = process.env.REACT_APP_API_URL;
    e.preventDefault();
    
    try {
      await axios.put(`${apiUrl}/api/beers/${id}`, beer);
      alert('Bière modifiée avec succès');
    } catch (error) {
      console.error('Erreur lors de la modification de la bière', error);
    }
  };

  const handleChange = (e) => {
    setBeer({ ...beer, [e.target.name]: e.target.value });
  };

  if (!beer) return <div>Chargement...</div>;

  return (
    <div>
      <h2>Modifier la bière</h2>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Nom"
          name="name"
          value={beer.name}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Description"
          name="description"
          value={beer.description}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Prix"
          name="price"
          value={beer.price}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Degré"
          name="degree"
          value={beer.degree}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="ID Brasserie"
          name="id_brasserie"
          value={beer.id_brasserie}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="URL de l'image"
          name="image_url"
          value={beer.image_url}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <Button type="submit" variant="contained" color="primary" style={{ marginTop: '20px' }}>
          Modifier la bière
        </Button>
      </form>
    </div>
  );
};

export default EditBeerForm;
