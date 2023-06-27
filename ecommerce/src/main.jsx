import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider} from 'react-router-dom'
import ErrorPage from './errorPage.jsx'
import App from './App.jsx'
import { Main } from './body'
import Product from './product.jsx'

const router = createBrowserRouter(
  [{
    path: "/",
    element: <App />,
    errorElement: <ErrorPage/>,
    children: [
      {
        path: "",
        element: <Main />
      },
      {
        path: "shirt",
        element: <Product />
      }, 
      {
        path: "watch",
        element: <Product />
      }
    ]
  }
]
);

// creating a browserRouter and passing routes to it


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* <App /> */}
    <RouterProvider router={router} />
  </React.StrictMode>,
)
