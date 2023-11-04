import { ArrowLeftIcon, ArrowRightIcon, MinusIcon } from '@chakra-ui/icons'
import {  Box ,Tr,Th,Table,TableCaption,TableContainer,Text, Thead, Tbody, Td, Tfoot, Checkbox, Grid, Select, GridItem, Button, CircularProgress, ButtonGroup, Center, ColorModeContext} from '@chakra-ui/react'
import { getNews } from '../services/api'
import React, {  useEffect, useState } from 'react'
import { useSelectedItems } from '../context/SelectedItemsContext'
import '../styles/table.css'

export interface locations{
  id: number;
  date : string;
  title : string;
  category: string;
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
  const [category, setCategory] = useState('');
  const [filterSort, setFilterSort] = useState(false);

  const [fromDate, setFromDate] = useState('');
  const [toDate, setToDate] = useState('');

  const handleFromDate = (event) => {
    setFromDate(event.target.value);
  };

  const handleToDate = (event) => {
    setToDate(event.target.value);
  };


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

 const handleFilterButton = () => {
  console.log('filtrando con las querys')
  console.log(toDate)
  console.log(fromDate)
  console.log(category)
  setFilterSort(current => !current);
 }

 const handleCleanFilters = () =>{
  setCategory('');
  setFromDate('');
  setToDate('');
  setFilterSort(sorted => !sorted);
 }

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
  


  const handleCategoriaChange = (event: React.ChangeEvent<HTMLSelectElement>) =>{
    const categoryId = event.target.id;
    if(categoryId === 'CategorySelect'){
      setCategory(event.target.value);
    }  
    console.log(category);
  }

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
          const data = await getNews(page, fromDate,toDate,category);
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
          const data = await getNews(page,fromDate,toDate, category);
          setNews(data);
          setLoading(false);

        }, )
      }catch (error){
        setLoading(false);
      }
    }
    fetchNews();
  }, [filterSort]);
  useEffect(() => {   
    async function fetchNews(){
      try{
        setTimeout(async () => {
          const data = await getNews(page,fromDate,toDate, category);
          setNews(data);
          setLoading(false);

        }, 0 ) 
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
          const data = await getNews(page, fromDate,toDate,category);
          setNews(data);
          setLoading(false);

        }, 0 ) 
      }catch (error){
        setLoading(false);
      }
    }
    fetchNews();
  }, [loading]);


  return (
    <Box pt={10}>

      <Text fontSize='2xl' className='TableTitle' fontFamily='Mukta Vaani' fontWeight='400' px={'10%'}> 
        <MinusIcon color={'#44cfe2'}/>  DOCUMENTOS DISPONIBLES PARA VISUALIZAR 
      </Text>

      <Grid px={'10%'} py='2%' templateColumns='repeat(7, 1fr)' gap={7}>
        <GridItem>
          <Text fontSize='l' fontFamily='Mukta Vaani' fontWeight='400'>Categoría</Text>
          <Select id='CategorySelect' placeholder='Categoría' value={category} onChange={handleCategoriaChange}>
            <option value='entretenimiento'>Entretenimiento</option>
            <option value='tecnologia'>Tecnología</option>
            <option value='medio_ambiente'>Medio Ambiente</option>
            <option value='ciencia'>Ciencia</option>
            <option value='politica'>Política</option>
            <option value='internacional'>Internacional</option>
            <option value='accidentes'>Accidentes</option>
            <option value='educacion'>Educación</option>
            <option value='salud'>Salud</option>
            <option value='economia'>Economía</option>
            <option value='deportes'>Deportes</option>


          </Select>
        </GridItem>
        <GridItem>
        <Text fontSize='l' fontFamily='Mukta Vaani' fontWeight='400' >Desde</Text>
        <input
          type="date"
          name="trip-start"
          value={fromDate}
          min="2000-01-01"
          max="2030-12-31"
          onChange={handleFromDate}
        />
      </GridItem>

      <GridItem>
        <Text fontSize='l' fontFamily='Mukta Vaani' fontWeight='400' >Hasta</Text>
        <input
          type="date"
          name="trip-start"
          value={toDate}
          min="2000-01-01"
          max="2030-12-31"
          onChange={handleToDate}
        />
      </GridItem>

        <GridItem>
          <Button onClick={handleFilterButton} > Filtrar </Button>
        </GridItem>
        <GridItem>
          <Button onClick={handleCleanButton}
          > Limpiar Mapa </Button>
        </GridItem>
        <GridItem>
          <Button onClick={handleVerButtonClick}>Ver </Button>
        </GridItem>
        <GridItem>
          <Button  onClick={handleCleanFilters} >Limpiar Filtros</Button>
        </GridItem>
        
      </Grid>
      
      <Box  pr={'10%'} pl={'10%'}>

        <TableContainer border='2px' borderRadius='3'>
        <Table  variant="striped" colorScheme={"teal"} >
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
            <Center bg='' h='300px'>
              <CircularProgress isIndeterminate color='#46c5a5' size='12rem'/>
            </Center>
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
                  <Td>{item.category.toUpperCase()}</Td>
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
          <Center w='40px' h='40px'  _dark={{color:'white'}}>
            <Box as='span' fontWeight='bold' fontSize='lg'>
              {page}
            </Box>
          </Center>
          <Button rightIcon={<ArrowRightIcon />} onClick={nextPage} >
            Siguiente
          </Button>
        </ButtonGroup>

      </Center>
    </Box>
  )
}
