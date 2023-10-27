import { Box, Button, Flex, Image, Stack, useColorMode } from '@chakra-ui/react'
import '../styles/header.css'
import React from 'react'



export const Header = () => {
    return (
      <Box px={10} bgColor={'#343434'} >
        <Flex  alignItems={'center'} justifyContent={'space-between'}>
          <Box>
            <a href='https://www.sophialt.org'>
              <Image src='\src\assets\logo_oscuro_2.png' alt='Logo sophia'  h='7.5rem'/>

            </a>
          </Box>
          <Flex alignItems={'center'} >
            <Stack direction={'row'} spacing={7}>
              <Button >
                {/* Añadir tema oscuro y claro */}
              </Button>
            </Stack>
          </Flex>
        </Flex>
      </Box>
     
    )
  }
  




