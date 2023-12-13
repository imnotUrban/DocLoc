import { Box, Button, Flex, Image, Stack, useColorMode } from '@chakra-ui/react'
import ThemeToggle from './ChangeTheme'
import '../styles/header.css'
import React from 'react'


export const Header = () => {
  const {colorMode} = useColorMode();
  const imagePath = colorMode === "dark" ? '../logo_oscuro_2.png': '../logo_claro.png' ;
  return (
      <Box px={10}  >
         {/* bgColor={'#343434'} */}
        <Flex  alignItems={'center'} justifyContent={'space-between'}>
          <Box>
            <a href='https://www.sophialt.org'>
              <Image src={imagePath} alt='Logo sophia'  h='7.5rem'/>

            </a>
          </Box>
          <Flex alignItems={'center'} >
            <Stack direction={'row'} spacing={7}>
              <ThemeToggle />
            </Stack>
          </Flex>
        </Flex>
      </Box>
     
    )
  }
  




