import React, { createContext, useContext, useState, ReactNode } from 'react';
// Asegúrate de importar la interfaz o tipo locations desde donde esté definida
import { locations } from '../components/DataTable';

interface SelectedItemsContextProps {
  selectedItems: locations[];
  setSelectedItems: React.Dispatch<React.SetStateAction<locations[]>>;


}

const SelectedItemsContext = createContext<SelectedItemsContextProps | undefined>(undefined);

export const useSelectedItems = () => {
  const context = useContext(SelectedItemsContext);
  if (!context) {
    throw new Error('Error en el context');
  }
  return context;
};

interface SelectedItemsProviderProps {
  children: ReactNode;
}

export const SelectedItemsProvider: React.FC<SelectedItemsProviderProps> = ({ children }) => {
  const [selectedItems, setSelectedItems] = useState<locations[]>([]);

  return (
    <SelectedItemsContext.Provider value={{ selectedItems, setSelectedItems }}>
      {children}
    </SelectedItemsContext.Provider>
  );
};
