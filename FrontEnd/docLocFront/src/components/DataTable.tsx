import { ArrowLeftIcon, ArrowRightIcon, MinusIcon } from '@chakra-ui/icons'
import { Box ,Tr,Th,Table,TableCaption,TableContainer,Text, Thead, Tbody, Td, Tfoot, Checkbox, Grid, Select, GridItem, Button, CircularProgress, ButtonGroup, Center} from '@chakra-ui/react'
import { getNews } from '../services/api'
import React, {  useEffect, useState } from 'react'
import { useSelectedItems } from '../context/SelectedItemsContext'
export interface locations{
  id: number;
  date : string;
  title : string;
  url: string;
  summary: string
  lat : number;
  lng : number;
}


export const DataTable: React.FC = () => {  
  
  const [page, setPages] = useState(1); // Se usa para paginar la página
  const {selectedItems, setSelectedItems} = useSelectedItems();
  const [checkItems, setCheckItems] = useState<locations[]>([]);
  const [news, setNews] = useState<locations[]>([]);
  const [loading, setLoading] = useState(true); // Se usa para esperar a que se haga la consulta para que cargue la tabla

  const nextPage = () => {
    setPages(page+1);
  }

  const prevPage = () => {
    setPages(page-1);
  }

 useEffect(() => {
 
   return () => {
     console.log('Se actualiza el arreglo de puntos en el mapa')
   }
 }, [selectedItems])
 

 const handleCleanButton = () => {
  setCheckItems([]);
  setSelectedItems([]);

 };



 const handleCheckboxChange = (item: locations) => {
  // Verificar si el elemento ya está en checkItems
  const exists = checkItems.find((checkItem) => checkItem.id === item.id);

  if (exists) {
    // Si el elemento ya está en la lista de seleccionados, quítalo
    setCheckItems(checkItems.filter((checkItem) => checkItem.id !== item.id));
    
  } else {
    // Si el elemento no está en la lista de seleccionados, agrégalo
    setCheckItems([...checkItems, item]);
  }
};


  const handleVerButtonClick = () => {
    setSelectedItems([...checkItems])
  }

  useEffect(() => {
    
    console.log(checkItems)
    return () => {
      console.log('checkItems' )
    }
  }, [checkItems])
  


  const handleDocuments = async (page: number) => {

    try{
      const newsData = await getNews(page);
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
          const data = await getNews(page);
          setNews(data);
          setLoading(false);

        }, )
      }catch (error){
        setLoading(false);
      }
    }
    fetchNews();
  }, []);
  useEffect(() => {   
    async function fetchNews(){
      try{
        setTimeout(async () => {
          const data = await getNews(page);
          setNews(data);
          setLoading(false);

        }, 0 ) //3000
      }catch (error){
        setLoading(false);
      }
    }
    fetchNews();
  }, [page]);
  useEffect(() => {   
    async function fetchNews(){
      try{
        setTimeout(async () => {
          const data = await getNews(page);
          setNews(data);
          setLoading(false);

        }, 0 ) //3000
      }catch (error){
        setLoading(false);
      }
    }
    fetchNews();
  }, [loading]);


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
          <Button onClick={handleCleanButton}
          > Limpiar </Button>
        </GridItem>
        <GridItem>
          <Button onClick={handleVerButtonClick}>Ver </Button>
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
            <Checkbox
              isChecked={checkItems.some((selectedItem) => selectedItem.id === item.id)}
              onChange={() => handleCheckboxChange(item)}
            />
      </Td>
      <Td>Categoría por ver</Td>
      <Td>{item.date}</Td>
      <Td>{item.title}</Td>
      <Td>{item.lat}</Td>
      <Td>{item.lng}</Td>
    </Tr>
  ))
  
  
  }
</Tbody>
            }
            
            <Tfoot>
              
            </Tfoot>
          </Table>
        </TableContainer>
      </Box>

      <Center>

        <ButtonGroup  mt={'3'} >
          <Button leftIcon={<ArrowLeftIcon />} onClick={prevPage}>
            Anterior
          </Button>
          <Center w='40px' h='40px' bg='tomato' color='white'>
            <Box as='span' fontWeight='bold' fontSize='lg'>
              {page}
            </Box>
          </Center>
          <Button leftIcon={<ArrowRightIcon />} onClick={nextPage} >
            Siguiente
          </Button>
        </ButtonGroup>

      </Center>
    </Box>
  )
}
