import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

const EditBreweryForm = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [brewery, setBrewery] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/api/breweries/${id}`)
      .then(response => {
        setBrewery(response.data);
      })
      .catch(error => {
        console.error('Erreur lors de la récupération de la brasserie:', error);
      });
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      await axios.put(`http://127.0.0.1:5000/api/breweries/${id}`, brewery);
      alert('Brasserie modifiée avec succès');
      navigate('/Brewery');  // Redirection vers la liste des brasseries après modification
    } catch (error) {
      console.error('Erreur lors de la modification de la brasserie', error);
    }
  };

  const handleChange = (e) => {
    setBrewery({ ...brewery, [e.target.name]: e.target.value });
  };

  if (!brewery) return <div>Chargement...</div>;

  return (
    <div>
      <h2>Modifier la brasserie</h2>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Nom"
          name="name"
          value={brewery.name}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Localisation"
          name="location"
          value={brewery.location}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Type de brasserie"
          name="brewery_type"
          value={brewery.brewery_type}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="URL de l'image"
          name="image_url"
          value={brewery.image_url}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <Button type="submit" variant="contained" color="primary" style={{ marginTop: '20px' }}>
          Modifier la brasserie
        </Button>
      </form>
    </div>
  );
};

export default EditBreweryForm;
