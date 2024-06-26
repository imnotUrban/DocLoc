import { useState } from "react"
import { useMapEvents } from "react-leaflet"
type Position = {
    lat: number;
    lng: number;
  };

export function LocationMarkerCenter() {
    const [position, setPosition] = useState<Position | null>(null)
    const map = useMapEvents({
      click() {
        map.locate()
      },
      locationfound(e) {
        setPosition(e.latlng)
        map.flyTo(e.latlng, map.getZoom())
      },
    })
  
    return position === null ? null : null
  }