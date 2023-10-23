import { MapView } from "./Components/MapView"
import { Header } from "./Components/Header"
import 'tailwindcss/tailwind.css';
import LocalizeForm from "./Components/LocalizeForm";
// w-600 h-400




export const App = () => {


  const handleSubmit = (title: string, body: string, url: string) => {
    // Aquí puedes manejar la lógica para enviar los datos del formulario, por ejemplo, enviar una solicitud a un servidor o almacenar los datos en el estado de la aplicación.
    console.log('Título:', title);
    console.log('Cuerpo:', body);
    console.log('URL:', url);
  };



  return (
    <div>
      
      <Header />
      
      <div className="grid grid-cols-3 gap-4" >
        <div className="col-span-2 bg-red-500 mx-3 mt-5">

          <MapView/>

        </div>

        <div className="form-style text-white rounded p-4 mt-5 mx-3 border-2">

          <LocalizeForm onSubmit={handleSubmit} />

        </div>
      
      </div>

      

    </div>
  )
}
