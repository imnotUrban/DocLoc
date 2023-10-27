import React from 'react'
import { Header } from './components/Header'
import { MapView } from './components/MapView'
import './App.css'
import { DataTable } from './components/DataTable'
export const App = () => {
  return (
    <div>
      <Header />
      <MapView />
      <DataTable />
    </div>
  )
}


