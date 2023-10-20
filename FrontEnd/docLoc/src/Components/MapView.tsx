import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import Markers from './Markers';
import {places} from '../data.json'

// const position: [number, number] = [-39.82047787588664, -73.24195718096213];
const mapCenter: [number, number] = [-39.82209496570248, -73.22759947406944];


// Convierte los datos de 'data.json' al formato esperado
const convertedPlaces = places.map((place) => ({
  name: place.name,
  geometry: [place.geometry[0], place.geometry[1]] as [number, number],
}));


export const MapView = () => {
  return (
    <MapContainer center={mapCenter} zoom={13} >
      <TileLayer
      attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    />

    <Markers places={convertedPlaces} ></Markers>


    </MapContainer>
  )
}


// <Marker position={position}>
//       <Popup>
//         La casa de la machita
//       </Popup>
//     </Marker>