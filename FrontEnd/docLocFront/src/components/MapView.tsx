import React, { useEffect, useRef, useState } from 'react'
import { MapContainer, TileLayer } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import { Box, Text } from '@chakra-ui/react';
import '../styles/map.css'
import { useSelectedItems } from '../context/SelectedItemsContext';
import Markers from './Markers';
import MarkerClusterGroup from 'react-leaflet-cluster';
import { LocationMarkerCenter } from '../utils/centerMap';
import { useMap } from 'react-leaflet/hooks'
import { LatLngTuple, LatLngBounds } from 'leaflet';

export const MapView = () => {

  const mapCenter: [number, number] = [-39.82209496570248, -73.22759947406944];
  const margin = 0.05;
  const corner1: LatLngTuple = [mapCenter[0] + margin, mapCenter[1] + margin];
  const corner2: LatLngTuple = [mapCenter[0] - margin, mapCenter[1] - margin];
  const initialBounds = new LatLngBounds(corner1, corner2);

  const {selectedItems} = useSelectedItems();
  const [mapBounds, setMapBounds] = useState(initialBounds);

  useEffect(() => {
    if (selectedItems.length > 0) {
      const coordinates = selectedItems.map((item) => [item.lat, item.lng]);
    
      const bounds = coordinates.reduce(
        (acc, cur) => acc.extend(cur),
        new LatLngBounds(coordinates[0], coordinates[0])
      );
      setMapBounds(bounds);
    } else {
      //setMapBounds(initialBounds); // Resetea los limites cuando no hay items seleccionados
    }
  }, [selectedItems]);

  function ChangeView({ bounds }) {
    const map = useMap();
    map.fitBounds(bounds); // ajusta el zoom para que se vean todos los lugares
    return null;
  }

  return (
    
    <Box className='mapContainer' >
      <Text id='Title' fontSize='3xl'  fontFamily='Mukta Vaani' fontWeight='400' > GEOLOCALIZACIÓN DE DOCUMENTOS TERRITORIALES</Text>
      <MapContainer
        bounds={mapBounds}
      >
        <ChangeView bounds={mapBounds} />
        <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>

      <MarkerClusterGroup >
        <Markers places={selectedItems} />
      </MarkerClusterGroup>

      <LocationMarkerCenter />

      </MapContainer>
    </Box>

  )
}
