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

  const marcadores = [{
    id: 1,
    date : "12",
    title : "XD",
    lat : 33.4,
    lng : 33.4,
  },{
    id: 3,
    date : "12",
    title : "XD",
    lat : 33.5,
    lng : 33.4,
  },{
    id: 2,
    date : "12",
    title : "XD",
    lat : 33.3,
    lng : 33.4,
  }

]



  const {selectedItems} = useSelectedItems();
  const mapRef = useRef(null); // Referencia al mapa
  
  useEffect(() => {
    console.log('Cambio la seleección de mapas y son: ', selectedItems) 
    
    



  }, [selectedItems]);



  return (
    
    <Box bgColor={'#343434'} className='mapContainer' >
      <Text fontSize='3xl' color='#f2f2f2' fontFamily='Mukta Vaani' fontWeight='400' align='right' pr='10%'> GEOLOCALIZACIÓN DE DOCUMENTOS TERRITORIALES</Text>
      <MapContainer center={mapCenter} zoom={13} >
        <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>

      <MarkerClusterGroup >
{/* ss */}
        <Markers places={marcadores} />
      </MarkerClusterGroup>
      </MapContainer>

    </Box>

  )




  
}

