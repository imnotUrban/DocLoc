import React from 'react'
import { Header } from './components/Header'
import { MapView } from './components/MapView'
import './App.css'
import { DataTable } from './components/DataTable'
import { SelectedItemsProvider } from './context/SelectedItemsContext'
import { Box } from '@chakra-ui/react'


export const App = () => {
  return (
    <Box>
        <Header />
        <MapView />
        <DataTable />
    </Box>
  )
}


