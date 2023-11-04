import React from 'react'
import { useColorMode, Button, IconButton } from '@chakra-ui/react'
import { MoonIcon, SunIcon } from '@chakra-ui/icons';
import '../styles/header.css'

const ThemeToggle = () => {
    const { colorMode, toggleColorMode } = useColorMode();
    return (
      <Button onClick={toggleColorMode} _light={{bgColor:'#cfd0d1'}}>
        {colorMode === "light" ?   <MoonIcon  /> :<SunIcon  />}
      </Button>
    );
  };
  
  export default ThemeToggle;