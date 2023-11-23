import React, { useEffect, useRef } from 'react'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import { Box, Text } from '@chakra-ui/react';
import '../styles/map.css'
import { useSelectedItems } from '../context/SelectedItemsContext';
import Markers from './Markers';
import MarkerClusterGroup from 'react-leaflet-cluster';


const mapCenter: [number, number] = [-39.82209496570248, -73.22759947406944];

export const MapView = () => {


  const {selectedItems} = useSelectedItems();
  
  useEffect(() => {
    console.log('Cambio la seleección de mapas y son: ', selectedItems) 

  }, [selectedItems]);



  return (
    
    <Box className='mapContainer' >
      <Text fontSize='3xl'  fontFamily='Mukta Vaani' fontWeight='400' > GEOLOCALIZACIÓN DE DOCUMENTOS TERRITORIALES</Text>
      <MapContainer center={mapCenter} zoom={6} >
        <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>

      <MarkerClusterGroup >
        <Markers places={selectedItems} />
      </MarkerClusterGroup>
      </MapContainer>

    </Box>

  )

  
}

