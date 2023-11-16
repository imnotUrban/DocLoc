import { extendTheme, ThemeConfig } from "@chakra-ui/react";
// @ts-ignore
const chakraTheme = extendTheme({
  config: {
    initialColorMode: "light", // Modo claro por defecto
  },
  styles: {
    global: (props) => ({
      body: {
        bg: props.colorMode === "dark" ? "#1D1D1B" : "red",
      },
    },
  },
  colors: {
    brand: {
      100: "#f7fafc", // Modo claro
      900: "#1D1D1B", // Modo oscuro
    },
  },
} as ThemeConfig); // Añade "as ThemeConfig" para establecer el tipo de retorno

export default chakraTheme;
