import { ArrowLeftIcon, ArrowRightIcon, MinusIcon } from '@chakra-ui/icons'
import {  Box ,Tr,Th,Table,TableCaption,TableContainer,Text, Thead, Tbody, Td, Tfoot, Checkbox, Grid, Select, GridItem, Button, CircularProgress, ButtonGroup, Center, ColorModeContext, Wrap,
  Modal, ModalOverlay, ModalContent, ModalHeader, ModalBody, ModalCloseButton,} from '@chakra-ui/react'
import { getNews } from '../services/apiService'
import React, {  useEffect, useState } from 'react'
import { useSelectedItems } from '../context/SelectedItemsContext'
import '../styles/table.css'
import { useSelectedItems } from '../context/SelectedItemsContext';
import { LatLngTuple, LatLngBounds } from 'leaflet';

export interface locations{
  id: number;
  date : string;
  title : string;
  category: string;
  location: string;
  url: string;
  summary: string
  lat : number;
  lng : number;
}

export const DataTable: React.FC = () => {  
  const [page, setPages] = useState(1); // Se usa para paginar la página
  const {selectedItems, setSelectedItems} = useSelectedItems(); // hook que alimenta el useContext con las noticias seleccionadas que deben mostrarse en el mapa
  const [news, setNews] = useState<locations[]>([]);
  const [loading, setLoading] = useState(true); // Se usa para esperar a que se haga la consulta para que cargue la tabla
  const [category, setCategory] = useState('');
  const [filterSort, setFilterSort] = useState(false);
  const [fromDate, setFromDate] = useState('');
  const [toDate, setToDate] = useState('');
  const [maxPage, setMaxPage] = useState(0);
  const [showPopup, setShowPopup] = useState(false); // Se encarga de decidir si se muestra el popup o no
  const [errorMessage, setErrorMessage] = useState(''); // Se encarga de selecionar el mensaje a mostrar en el popup de acuerdo al error

  const mapCenter: [number, number] = [-39.82209496570248, -73.22759947406944];
  const margin = 0.05;
  const corner1: LatLngTuple = [mapCenter[0] + margin, mapCenter[1] + margin];
  const corner2: LatLngTuple = [mapCenter[0] - margin, mapCenter[1] - margin];
  const bounds = new LatLngBounds(corner1, corner2);

  const handleFromDate = (event) => {
    setFromDate(event.target.value);
  };

  const handleToDate = (event) => {
    setToDate(event.target.value);
  };

  const nextPage = () => {
    setPages(page + 1);
  }

  const prevPage = () => {
    setPages(page - 1);
  }

 const handleCleanButton = () => {
  setSelectedItems([]);
 };

 const handleFilterButton = () => {
  setFilterSort(current => !current);
  setPages(1);
 }

 const handleCleanFilters = () =>{
  setCategory('');
  setFromDate('');
  setToDate('');
  setFilterSort(sorted => !sorted);
  setPages(1);
 }

 const handleCheckboxChange = (item: locations) => {
  // Verificar si el elemento ya está en checkItems
  const exists = selectedItems.find((selectedItem) => selectedItem.id === item.id);

  if (exists) {
    // Si el elemento ya está en la lista de seleccionados, quítalo
    setSelectedItems(selectedItems.filter((selectedItem) => selectedItem.id !== item.id));
    
  } else {
    // Si el elemento no está en la lista de seleccionados, agrégalo
    setSelectedItems([...selectedItems, item]);
  }
};

  const handleCategoriaChange = (event: React.ChangeEvent<HTMLSelectElement>) =>{
    const categoryId = event.target.id;
    if(categoryId === 'CategorySelect'){
      setCategory(event.target.value);
    }  
    console.log(category);
  }

  useEffect(()=> {
    console.log(showPopup);
  }, showPopup)

  const handleDocuments = async (page: number) => {
    async function fetchNews(){
      try{
        setTimeout(async () => {
          const {status, data} = await getNews(page, fromDate, toDate, category);
          if(status === 0) {
            setNews(data.doc);
            setMaxPage(Math.ceil(data.count/10));
            setLoading(false);
            setShowPopup(false);
          } else {
            if(status === 1) {
              setErrorMessage('La solicitud a la API no fue exitosa');
            } else {
              setErrorMessage('Error al obtener los documentos');
            }
            //Muestra un popup de error en caso de que no pueda cargar los documentos
            setShowPopup(true);
          }
        }, 0)
      }catch (error){
        setLoading(false);
      }
    }
    fetchNews();
  };


  /**
   * Carga inicial de los documentos
   */
  useEffect(() => {   
    handleDocuments(page);
  }, []);

  useEffect(() => {
    handleDocuments(page);
    //setSelectedItems(bounds);
  }, [filterSort, loading, page]);

  const Popup = (
    <Modal isOpen={showPopup} onClose={() => setShowPopup(false)}>
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>Error!</ModalHeader>
        <ModalCloseButton />
        <ModalBody>
          {errorMessage}
        </ModalBody>
      </ModalContent>
    </Modal>
  );

  return (
    <Box>
        <Text id='TableTitle' fontSize='2xl' className='TableTitle' fontFamily='Mukta Vaani' fontWeight='400'> 
          <MinusIcon color={'#44cfe2'}/>  DOCUMENTOS DISPONIBLES PARA VISUALIZAR 
        </Text>
        {showPopup && Popup}      
  <Grid templateColumns={['repeat(1, 1fr)', 'repeat(2, 1fr)', 'repeat(3, 1fr)', 'repeat(6, 1fr)']} gap={4} py='2%'>
  <GridItem >
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
      id='FromDate'
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
      id='ToDate'
      type="date"
      name="trip-start"
      value={toDate}
      min="2000-01-01"
      max="2030-12-31"
      onChange={handleToDate}
    />
  </GridItem>

  <GridItem colSpan={[2, null, null, 1]}>
    <Button id='ButtonFilter' onClick={handleFilterButton} > Filtrar </Button>
  </GridItem>
  {/* <GridItem colSpan={[2, null, null, 1]}>
    <Button onClick={handleCleanButton}> Limpiar Mapa </Button>
  </GridItem> */}
  <GridItem colSpan={[2, null, null, 1]}>
    <Button onClick={handleCleanFilters}>Limpiar Filtros</Button>
  </GridItem>
</Grid>

      <Box  pr={'0%'}  maxHeight="65vh" overflowY="auto" >

        <TableContainer border='2px' borderRadius='3'   >
        <Table size='sm' variant="striped" colorScheme={"teal"}>
            <TableCaption>Documentos geolocalizables</TableCaption>
            <Thead>
            <Tr>
              <Th width="10%">VER</Th>
              <Th width="10%">CATEGORÍA</Th>
              <Th width="10%">FECHA</Th>
              <Th width="50%">TÍTULO</Th>
              <Th width="10%"> DIRECCIÓN</Th>
              {/* <Th width="10%">LATITUD</Th>
              <Th width="10%">LONGITUD</Th> */}
            </Tr>
            </Thead>
            {loading? 
            (
            <Td colSpan={6} h='300px'>
              <CircularProgress isIndeterminate color='#46c5a5' size='12rem'/>
            </Td>
            )
            :
            
            <Tbody>
              {news.map((item, index) => (
                <Tr key={item.id}>
                  <Td style={{ whiteSpace: "normal" }} width='10%'>
                    <Checkbox
                      isChecked={selectedItems.some((selectedItem) => selectedItem.id === item.id)}
                      onChange={() => handleCheckboxChange(item)}
                        />
                  </Td>
                  <Td id={`CategoryId${index}`} style={{ whiteSpace: "normal" }} width='10%'>{item.category.toUpperCase()}</Td>
                  <Td id={`DateId${index}`} style={{ whiteSpace: "normal" }} width='10%'>{item.date}</Td>
                  <Td id={`TitleId${index}`}  style={{ whiteSpace: "normal" }} width='50%'>{item.title}</Td>
                  <Td style={{ whiteSpace: "normal" }} width='10%'>{item.location}</Td>
                  {/* <Td style={{ whiteSpace: "normal" }} width='10%'>{item.lat}</Td>
                  <Td style={{ whiteSpace: "normal" }} width='10%'>{item.lng}</Td> */}
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
          <Button id='ButtonPrevious' isDisabled= {page===1} leftIcon={<ArrowLeftIcon />} onClick={prevPage}>
            Anterior
          </Button>
          <Center w='40px' h='40px'  _dark={{color:'white'}}>
            <Box as='span' fontWeight='bold' fontSize='lg'>
              {page}
            </Box>
          </Center>
          <Button id='ButtonNext' isDisabled={page === maxPage}  rightIcon={<ArrowRightIcon />} onClick={nextPage} >
            Siguiente
          </Button>
        </ButtonGroup>

      </Center>
    </Box>
  )
}
