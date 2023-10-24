import { useState, ChangeEvent, FormEvent } from "react";
import 'tailwindcss/tailwind.css';


interface LocalizeFormProps {
  onSubmit: (title: string, body: string, url: string) => void;
}



const LocalizeForm: React.FC<LocalizeFormProps> = ({ onSubmit }) => {


  const [title, setTitle] = useState<string>('');
  const [body, setBody] = useState<string>('');
  const [url, setUrl] = useState<string>('');


  const handleTitleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setTitle(e.target.value);
  };

  const handleBodyChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    setBody(e.target.value);
  };

  const handleUrlChange = (e: ChangeEvent<HTMLInputElement>) => {
    setUrl(e.target.value);
  };

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    onSubmit(title, body, url);
    // Limpiar los campos después de enviar el formulario
    setTitle('');
    setBody('');
    setUrl('');
  };


  return (

    <div>
      <h3 className="text-center title-form"> Geolocaliza</h3>
      <div className="form-style">

        <form onSubmit={handleSubmit}>
          <div className="mt-10">
            <label className="mx-3">Título de la noticia</label>
            <input className="input-form mt-1" type="text" value={title} onChange={handleTitleChange} />
          </div>
          <div className="mt-10">
            <label className="mx-3">Cuerpo de la noticia</label>
            <textarea  className= "input-form mt-1 resize-none" value={body} onChange={handleBodyChange} />
          </div>
          <div className="mt-10">
            <label className="mx-3">URL de la noticia</label>
            <input className="input-form mt-1" type="text" value={url} onChange={handleUrlChange} />
          </div>
          <div className="button-section flex justify-between">
            
            <button className="button-form border rounded-xl p-3"type="submit">Enviar</button>

            <button className="button-form border rounded-xl p-3"type="submit">Mostrar</button>
          </div>
        </form>

      </div>
    </div>
  )
}


export default LocalizeForm
