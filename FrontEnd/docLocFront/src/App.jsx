import React from 'react'
import { Header } from './components/Header'
import { MapView } from './components/MapView'
import './App.css'
import { DataTable } from './components/DataTable'
import { SelectedItemsProvider } from './context/SelectedItemsContext'


export const App = () => {
  return (
    <div>
      <SelectedItemsProvider>
        <Header />
        <MapView />
        <DataTable />
      </SelectedItemsProvider>
    </div>
  )
}


