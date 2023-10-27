import { MinusIcon } from '@chakra-ui/icons'
import { Box ,Tr,Th,Table,TableCaption,TableContainer,Text, Thead, Tbody, Td, Tfoot, Checkbox, Grid, Select, GridItem, Button} from '@chakra-ui/react'
import React from 'react'
export const DataTable = () => {
  return (
    <Box bgColor={'#343434'} pt={10}>

      <Text fontSize='2xl' color='#f2f2f2' fontFamily='Mukta Vaani' fontWeight='400' px={'10%'}> 
        <MinusIcon color={'#44cfe2'}/>  DOCUMENTOS DISPONIBLES PARA VISUALIZAR 
      </Text>

      <Grid px={'10%'} py='2%' templateColumns='repeat(6, 1fr)' gap={7}>
        <GridItem>
          <Text fontSize='l' fontFamily='Mukta Vaani' fontWeight='400' color='white'>Categoría</Text>
          <Select placeholder='Categoría'>
            <option value='option1'>Option 1</option>
            <option value='option2'>Option 2</option>
            <option value='option3'>Option 3</option>
          </Select>
        </GridItem>
        <GridItem>
          <Text fontSize='l' fontFamily='Mukta Vaani' fontWeight='400' color='white'>Desde</Text>
          <input type="date" id="start" name="trip-start" value="" min="2018-01-01" max="2018-12-31" />
        </GridItem>
        <GridItem>
          <Text fontSize='l' fontFamily='Mukta Vaani' fontWeight='400' color='white'>Hasta</Text>
          <input type="date" id="start" name="trip-start" value="" min="2018-01-01" max="2018-12-31" />
        </GridItem>
        <GridItem>
          <Button> FILTRAR </Button>
        </GridItem>
        <GridItem>
          <Button> Limpiar </Button>
        </GridItem>
        <GridItem>
          <Button>Ver </Button>
        </GridItem>
        
      </Grid>
      
      <Box  pr={'10%'} pl={'10%'}>

        <TableContainer bgColor='#f2f2f2'>
          <Table variant='striped' colorScheme='teal'>
            <TableCaption>Documentos geolocalizables</TableCaption>
            <Thead>
              <Tr>
                <Th>VER</Th>
                <Th>CATEGORÍA</Th>
                <Th>FECHA</Th>
                <Th>TÍTULO</Th>
                <Th>LATITUD</Th>
                <Th>LONGITUD</Th>
              </Tr>
            </Thead>
            <Tbody>
              <Tr>
                <Td>
                  <Checkbox></Checkbox>
                </Td>
                <Td>deporte </Td>
                <Td> 24/ 12/ 2020</Td>
                <Td> la macha hace una maraton de 20 km</Td>
                <Td> 15.1212338</Td>
                <Td> 12.4949838</Td>
              </Tr>
              <Tr>
                <Td>
                  <Checkbox></Checkbox>
                </Td>
                <Td>deporte </Td>
                <Td> 24/ 12/ 2020</Td>
                <Td> la macha hace una maraton de 20 km</Td>
                <Td> 15.1212338</Td>
                <Td> 12.4949838</Td>
              </Tr>
              <Tr>
                <Td>
                  <Checkbox></Checkbox>
                </Td>
                <Td>deporte </Td>
                <Td> 24/ 12/ 2020</Td>
                <Td> la macha hace una maraton de 20 km</Td>
                <Td> 15.1212338</Td>
                <Td> 12.4949838</Td>
              </Tr>
              <Tr>
                <Td>
                  <Checkbox></Checkbox>
                </Td>
                <Td>deporte </Td>
                <Td> 24/ 12/ 2020</Td>
                <Td> la macha hace una maraton de 20 km</Td>
                <Td> 15.1212338</Td>
                <Td> 12.4949838</Td>
              </Tr>
              
            </Tbody>
            <Tfoot>
              <Tr>
                <Th>VER</Th>
                <Th>CATEGORÍA</Th>
                <Th>FECHA</Th>
                <Th>TÍTULO</Th>
                <Th>LATITUD</Th>
                <Th>LONGITUD</Th>
              </Tr>
            </Tfoot>
          </Table>
        </TableContainer>
      </Box>




    </Box>
  )
}
