export async function getNews(page: number = 1, fromDate: string = '', toDate: string = '', category: string = '') {
  try {
    //let url = `http://127.0.0.1:8000/query?page=${page}`;
    let url = `http://0.0.0.0:5001/query?page=${page}`; // Docker URL

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
