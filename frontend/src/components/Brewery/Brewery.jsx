import React, { useEffect, useState } from 'react';

const Brewery = () => {
  const [brasseries, setBrasseries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBrasseries = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/brasseries');
        
        if (!response.ok) {
          throw new Error('Erreur lors de la récupération des brasseries');
        }

        const data = await response.json();

        console.log("Données des brasseries :", data);  // Vérifiez ici les données retournées

        setBrasseries(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchBrasseries();
  }, []);  

  if (loading) {
    return <div>Chargement...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>Liste des Brasseries</h1>
      <div className="brewery-list">
        {brasseries.length === 0 ? (
          <p>Aucune brasserie disponible.</p>
        ) : (
          brasseries.map((brasserie) => (
            <div key={brasserie.id} className="brewery-card">
              <img src={brasserie.image_url} alt={brasserie.name} />
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
