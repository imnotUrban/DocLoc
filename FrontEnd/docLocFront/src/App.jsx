import React from 'react'
import { Header } from './components/Header'
import { MapView } from './components/MapView'
import './App.css'
import { DataTable } from './components/DataTable'
import { SelectedItemsProvider } from './context/SelectedItemsContext'
import { Box, Flex } from '@chakra-ui/react'


export const App = () => {
  return (
    <Box>
      <Header />
      <Flex>
        <Box flex="3" p="2">
          <MapView />
        </Box>
        <Box flex="1" p="2">
          <DataTable  />
        </Box>
      </Flex>
    </Box>
  );
};



