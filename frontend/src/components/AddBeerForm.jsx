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
  const [errors, setErrors] = useState({});

  const validateForm = () => {
    let newErrors = {};
    if (!name) newErrors.name = 'Le nom est requis';
    if (!description) newErrors.description = 'La description est requise';
    if (!price || isNaN(price)) newErrors.price = 'Le prix doit être un nombre valide';
    if (!degree || isNaN(degree)) newErrors.degree = 'Le degré doit être un nombre valide';
    if (!idBrasserie || isNaN(idBrasserie)) newErrors.idBrasserie = 'L\'ID brasserie doit être un nombre valide';
    if (!imageUrl) newErrors.imageUrl = 'L\'URL de l\'image est requise';
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    const apiUrl = process.env.REACT_APP_API_URL;

    e.preventDefault();
    
    if (!validateForm()) return;
    
    const newBeer = {
      name,
      description,
      price: parseFloat(price),
      degree: parseFloat(degree),
      id_brasserie: parseInt(idBrasserie),
      image_url: imageUrl,
    };

    try {
      await axios.post(`${apiUrl}/api/beers`, newBeer);
      alert('Bière ajoutée avec succès');
      setName('');
      setDescription('');
      setPrice('');
      setDegree('');
      setIdBrasserie('');
      setImageUrl('');
      setErrors({});
    } catch (error) {
      alert('Erreur lors de l\'ajout de la bière. Vérifiez la console pour plus de détails.');
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
          error={!!errors.name}
          helperText={errors.name}
        />
        <TextField
          label="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          fullWidth
          margin="normal"
          error={!!errors.description}
          helperText={errors.description}
        />
        <TextField
          label="Prix"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          fullWidth
          margin="normal"
          error={!!errors.price}
          helperText={errors.price}
        />
        <TextField
          label="Degré"
          value={degree}
          onChange={(e) => setDegree(e.target.value)}
          fullWidth
          margin="normal"
          error={!!errors.degree}
          helperText={errors.degree}
        />
        <TextField
          label="ID Brasserie"
          value={idBrasserie}
          onChange={(e) => setIdBrasserie(e.target.value)}
          fullWidth
          margin="normal"
          error={!!errors.idBrasserie}
          helperText={errors.idBrasserie}
        />
        <TextField
          label="URL de l'image"
          value={imageUrl}
          onChange={(e) => setImageUrl(e.target.value)}
          fullWidth
          margin="normal"
          error={!!errors.imageUrl}
          helperText={errors.imageUrl}
        />
        <Button type="submit" variant="contained" color="primary" style={{ marginTop: '20px' }}>
          Ajouter la bière
        </Button>
      </form>
    </div>
  );
};

export default AddBeerForm;