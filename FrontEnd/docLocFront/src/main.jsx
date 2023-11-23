import React from 'react'
import ReactDOM from 'react-dom/client'
import {App} from './App.jsx'
import {CSSReset, ChakraProvider,ColorModeScript,extendTheme } from '@chakra-ui/react'
import { SelectedItemsProvider } from './context/SelectedItemsContext'
const theme = extendTheme({
  config: {
    initialColorMode: "ligth", // Modo claro por defecto
  },
  styles: {
    global: (props) => ({
      body: {
        bg: props.colorMode === "dark" ? "#1D1D1B" : "#f2f2f2",
        color: props.colorMode === "dark" ? "#f2f2f2": "#1D1D1B",
      },
    }),
  },
  colors: {
    brand: {
      100: "#f7fafc", // Modo claro
      900: "#1D1D1B", // Modo oscuro
    },teal: {
      50: "#E0F7FA",
      100: "#B2EBF2",
      200: "#80DEEA",
      300: "#4DD0E1",
      400: "#26C6DA",
      500: "#44cfe2", // Color de la tabla
      600: "#00ACC1",
      700: "#0097A7",
      800: "#00838F",
      900: "#006064",
    },

  },
});

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <SelectedItemsProvider>
      <ChakraProvider theme={theme}>
        <CSSReset />
        <App />
      </ChakraProvider>
    </SelectedItemsProvider>
  </React.StrictMode>,
)
