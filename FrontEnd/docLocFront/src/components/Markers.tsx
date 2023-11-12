import { Card, CardBody, CardHeader, Heading, Text, CardFooter, Button } from '@chakra-ui/react';
import React from 'react';
import { Marker, Popup } from 'react-leaflet';



interface Place {
  id: number;
  date : string;
  title : string;
  url: string;
  category: string;
  summary: string;
  lat : number;
  lng : number;
}

interface MarkersProps {
  places: Place[];
}

const Markers: React.FC<MarkersProps> = (props) => {
  console.log(props)
  const { places } = props;

  const markers = places.map((place: Place, i: number) => (
    <Marker
      key={place.id}
      position={[place.lat, place.lng]}
    >
        <Popup > 
          <Card bgColor={'white'} color='black' align='center'>
            <CardHeader>
              <Heading size='xs'> {place.title} </Heading>
            </CardHeader>
            <CardBody>
              <Text>...{place.summary}...</Text>
            </CardBody>
            <CardFooter>
              <Button  ><a href={place.url} target="_blank"> Origen </a></Button>
            </CardFooter>

          </Card>
        </Popup>
    </Marker>
  ));

  return markers;
};

export default Markers;
