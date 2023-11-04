import React from 'react'
import ReactDOM from 'react-dom/client'
import {App} from './App.jsx'
import {ChakraProvider,extendTheme } from '@chakra-ui/react'
import { SelectedItemsProvider } from './context/SelectedItemsContext'

const colors = {
  brand: {
    900: '#1a365d',
    800: '#153e75',
    700: '#2a69ac',
  },
}

const theme = extendTheme({ colors })



ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <SelectedItemsProvider>
      <ChakraProvider theme={theme}>
        <App />
      </ChakraProvider>
    </SelectedItemsProvider>
  </React.StrictMode>,
)
