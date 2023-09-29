import googlemaps

gmaps = googlemaps.Client(key='AIzaSyC32hc-i4xyV5nTFBWGfu3pFUFYci_LZMw')
place = "O'Higgins"
geocode_result = gmaps.geocode(place)
if geocode_result:
    lat = str(geocode_result[0]["geometry"]["location"]["lat"])
    lng = str(geocode_result[0]["geometry"]["location"]["lng"]) 
    print(f'Lugar: {place}\nLat: {lat}\nLng: {lng}')
else:
    print(place)
    print(geocode_result)