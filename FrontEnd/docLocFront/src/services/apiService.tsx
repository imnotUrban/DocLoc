export async function getNews(page: number = 1, fromDate: string = '', toDate: string = '', category: string = '') {
  try {
    let url = `http://localhost:5001/api/query?page=${page}`; // llevar a .env pronto...

    if (category !== '') {
      url += `&cat=${category}`;
    }
    if (fromDate !== '') {
      url += `&from_=${fromDate}`;
    }
    
    if (toDate !== '') {
      url += `&to_=${toDate}`;
    }

    const response = await fetch(url);

    if (!response.ok) {
      throw new Error('La solicitud a la API no fue exitosa.');
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error al obtener los documentos:', error);
    throw error;
  }
}
