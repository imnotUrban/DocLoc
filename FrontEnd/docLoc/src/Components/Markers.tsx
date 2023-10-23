import React from 'react';
import { Marker, Popup } from 'react-leaflet';



interface Place {
  name: string;
  geometry: [number, number];
}

interface MarkersProps {
  places: Place[];
}

const Markers: React.FC<MarkersProps> = (props) => {
  const { places } = props;

  const markers = places.map((place: Place, i: number) => (
    <Marker
      key={i}
      position={place.geometry}
    >
        <Popup>{place.name}  <br/> a </Popup>
    </Marker>
  ));

  return markers;
};

export default Markers;
