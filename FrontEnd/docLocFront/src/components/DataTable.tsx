import { MinusIcon } from '@chakra-ui/icons'
import { Box ,Tr,Th,Table,TableCaption,TableContainer,Text, Thead, Tbody, Td, Tfoot, Checkbox, Grid, Select, GridItem, Button, CircularProgress} from '@chakra-ui/react'
import { getAllNews } from '../services/api'
import React, {  useEffect, useState } from 'react'

export interface locations{
  id: number;
  date : string;
  title : string;
  lat : number;
  lng : number;
}


export const DataTable: React.FC = () => {

  
  
  
  const [selectedItems, setSelectedItems] = useState<locations[]>([]); // Lugares que se renderizarán en el mapa
  const [news, setNews] = useState<locations[]>([]);
  const [loading, setLoading] = useState(true); // Se usa para esperar a que se haga la consulta para que cargue la tabla


  const handleCheckboxChange = (item: locations) => {
    if (selectedItems.includes(item)) {
      // Si el elemento ya está en la lista de seleccionados, quítalo
      setSelectedItems(selectedItems.filter((selectedItem) => selectedItem !== item));
    } else {
      // Si el elemento no está en la lista de seleccionados, agrégalo
      setSelectedItems([...selectedItems, item]);
    }
  };

  const handleButtonClick = () => {
    console.log(selectedItems); // Acá debería ir un useEffect para ver que cambió
  }



  const handleDocuments = async () => {

    try{
      const newsData = await getAllNews();
      setNews(newsData);
      
    }catch(error){
      //Mostrar un popup de error en caso de que no pueda cargar los documentos
      //TODO
      console.log('no cargan los docs');
    }
  };


  /**
   * Carga inicial de los documentos
   */
  useEffect(() => {   
    async function fetchNews(){
      try{
        setTimeout(async () => {
          const data = await getAllNews();
          setNews(data);
          setLoading(false);

        }, 3000)
      }catch (error){
        setLoading(false);
      }
    }
    fetchNews();
  }, []);


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
          <Button onClick={handleButtonClick}>Ver </Button>
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
            {loading? 
            (
              
            <CircularProgress isIndeterminate color='green.300' size='12rem'/>
            
            )
            :
            
            <Tbody>
              {news.map((item) => (
                <Tr key={item.id}>
                  <Td>
                    <Checkbox checked={selectedItems.find((selectedItem) => selectedItem.id === item.id) ? true : false}
                  onChange={() => handleCheckboxChange(item)}>

                    </Checkbox>
                  </Td>
                  <Td>Categoría por ver</Td>
                  <Td>{item.date}</Td>
                  <Td>{item.title}</Td>
                  <Td>{item.lat}</Td>
                  <Td>{item.lng}</Td>
                </ Tr>
              ))}

              
            </Tbody>
            }
            
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
