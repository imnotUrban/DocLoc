import { extendTheme, ThemeConfig } from "@chakra-ui/react";
// @ts-ignore
const chakraTheme = extendTheme({
  config: {
    initialColorMode: "light", // Modo claro por defecto
  },
  styles: {
    global: (props) => ({
      body: {
        bg: props.colorMode === "dark" ? "gray.900" : "red",
      },
    },
  },
  colors: {
    brand: {
      100: "#f7fafc", // Modo claro
      900: "#171923", // Modo oscuro
    },
  },
} as ThemeConfig); // Añade "as ThemeConfig" para establecer el tipo de retorno

export default chakraTheme;
