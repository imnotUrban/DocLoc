
//PONER EN .ENV
export async function getNews(page: number) {
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/news/page/?page=${page}`);
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
  