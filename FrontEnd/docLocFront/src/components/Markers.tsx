import React from 'react';
import { Marker, Popup } from 'react-leaflet';



interface Place {
  id: number;
  date : string;
  title : string;
  lat : number;
  lng : number;
}

interface MarkersProps {
  places: Place[];
}

const Markers: React.FC<MarkersProps> = (props) => {
  const { places } = props;

  const markers = places.map((place: Place, i: number) => (
    <Marker
      key={place.id}
      position={[place.lat, place.lng]}
    >
        <Popup> <b>{place.title} </b> <br/> <i>... cuando pepito fue a comprar pan descubrio que nunca tuvo plata ...</i> <br/> <a href='www.pepitogordo.com'> LINK A LA NOTICIA </a> </Popup>
    </Marker>
  ));

  return markers;
};

export default Markers;
