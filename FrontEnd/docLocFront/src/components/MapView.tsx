import React from 'react'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import { Box, Text } from '@chakra-ui/react';
import '../styles/map.css'


const mapCenter: [number, number] = [-39.82209496570248, -73.22759947406944];

export const MapView = () => {
  return (
    
    <Box bgColor={'#343434'} className='mapContainer' >
      <Text fontSize='3xl' color='#f2f2f2' fontFamily='Mukta Vaani' fontWeight='400' align='right' pr='10%'> GEOLOCALIZACIÓN DE DOCUMENTOS TERRITORIALES</Text>
      <MapContainer center={mapCenter} zoom={13} >
        <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>

      </MapContainer>

    </Box>

  )
}

