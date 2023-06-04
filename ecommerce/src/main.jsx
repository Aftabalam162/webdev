import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import App from './App.jsx'

const router = createBrowserRouter(
  [{
    path: "/",
    element: <App />
  },
  {
    path: "/Home",
    element: <h1>"This is the nicest shirt in the town"</h1>
  }

]
);


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
    {/* <RouterProvider router={router} /> */}
  </React.StrictMode>,
)
