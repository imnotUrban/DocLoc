enum ApiRequestStatus {
  Success = 0, // La solicitud a la API fue exitosa
  RequestUnsuccessful = 1, // La solicitud a la API no fue exitosa
  DocumentRetrievalError = 2 // Error al obtener los documentos
}

export async function getNews(page: number = 1, fromDate: string = '', toDate: string = '', category: string = '') {
  try {
    //let url = `http://127.0.0.1:8000/query?page=${page}`;
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
      return {status: ApiRequestStatus.RequestUnsuccessful}
    }

    const data = await response.json();
    return {status: ApiRequestStatus.Success, data: data};
  } catch (error) {
    console.error('Error al obtener los documentos:', error);
    return {status: ApiRequestStatus.DocumentRetrievalError};
  }
}