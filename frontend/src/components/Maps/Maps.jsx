import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import './Maps.css';

// Import des images de l'icône Leaflet pour corriger le problème d'affichage dans React
import iconUrl from 'leaflet/dist/images/marker-icon.png';
import iconShadowUrl from 'leaflet/dist/images/marker-shadow.png';

// Fix pour l'icône par défaut de Leaflet avec React
const DefaultIcon = L.icon({
    iconUrl: iconUrl,
    shadowUrl: iconShadowUrl,
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41],
});

L.Marker.prototype.options.icon = DefaultIcon;

export default function Maps() {
    const [brasseries, setBrasseries] = useState([]);
    const apiUrl = process.env.REACT_APP_API_URL;

    useEffect(() => {
        fetch(`${apiUrl}/api/brasseries`)
            .then((res) => res.json())
            .then((data) => setBrasseries(data))
            .catch((err) => console.error('Erreur API :', err));
    }, []);

    const brasseriesAvecCoordonnees = brasseries.filter(
        (b) => b.latitude != null && b.longitude != null
    );

    return (
        <div>
            <h1>Carte des brasseries</h1>
            <div className="map-wrapper">
                <MapContainer center={[48.85, 2.35]} zoom={6} className="map-container">
                    <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
                    {brasseriesAvecCoordonnees.map((b, index) => (
                        <Marker key={index} position={[b.latitude, b.longitude]}>
                            <Popup>
                                <img
                                    src={b.image_url}
                                    alt={b.name}
                                    style={{
                                        width: '100px',
                                        height: '100px',
                                        objectFit: 'cover',
                                        display: 'block',
                                        marginBottom: '0.5rem',
                                        borderRadius: '6px',
                                    }}
                                />
                                <strong>{b.name}</strong><br />
                                {b.description}
                            </Popup>
                        </Marker>
                    ))}
                </MapContainer>
            </div>
        </div>
    );

}