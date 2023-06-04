import { useState } from 'react'
import { Navbar } from './nav'
import { Outlet } from 'react-router-dom'
import { Footer } from './footer'

export default function App() {

  return (
    <>
      <Navbar />
      {/* <Main /> */}
      < Outlet />
      <Footer />
    </>
  )
}

