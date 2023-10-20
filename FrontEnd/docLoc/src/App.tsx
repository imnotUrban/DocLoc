import { Form } from "./Components/Form"
import { MapView } from "./Components/MapView"
import { Header } from "./Components/Header"
import 'tailwindcss/tailwind.css';
// w-600 h-400
export const App = () => {
  return (
    <div>
      
      <Header />
      
      <div className="grid grid-cols-3 gap-4" >
        <div className="col-span-2 bg-red-500">

          <MapView/>

        </div>

        <div className="bg-blue-500 text-white border rounded p-4">

          <Form />

        </div>
      
      </div>

      

    </div>
  )
}
