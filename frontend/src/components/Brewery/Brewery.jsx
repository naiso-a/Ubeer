import React, { useEffect, useState } from 'react';
import './Brewery.css'; // Assure-toi d’importer ce fichier CSS

const Brewery = () => {
  const [brasseries, setBrasseries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBrasseries = async () => {
      const apiUrl = process.env.REACT_APP_API_URL;

      try {
        const response = await fetch(`${apiUrl}/api/brasseries`);

        if (!response.ok) {
          throw new Error('Erreur lors de la récupération des brasseries');
        }

        const data = await response.json();
        setBrasseries(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchBrasseries();
  }, []);

  if (loading) return <div>Chargement...</div>;
  if (error) return <div>{error}</div>;

  return (
      <div className="brewery-page">
        <h1>Liste des Brasseries</h1>
        <div className="brewery-list">
          {brasseries.length === 0 ? (
              <p>Aucune brasserie disponible.</p>
          ) : (
              brasseries.map((brasserie) => (
                  <div key={brasserie.id} className="brewery-card">
                    <img
                        src={brasserie.image_url}
                        alt={brasserie.name}
                        className="brewery-image"
                    />
                    <h3>{brasserie.name}</h3>
                    <p>{brasserie.description}</p>
                  </div>
              ))
          )}
        </div>
      </div>
  );
};

export default Brewery;
