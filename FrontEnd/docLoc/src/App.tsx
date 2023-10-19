import { Form } from "./Components/Form"
import { Map } from "./Components/Map"
import { Header } from "./Components/Header"
import 'tailwindcss/tailwind.css';

export const App = () => {
  return (
    <div>
      
      <Header />
      
      <div className="grid grid-cols-3 gap-4" >
        <div className="col-span-2">

          <Map/>

        </div>

        <div className="bg-blue-500 text-white border rounded p-4">

          <Form />

        </div>
      
      </div>

      

    </div>
  )
}
