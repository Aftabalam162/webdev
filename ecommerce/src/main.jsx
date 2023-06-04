import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider} from 'react-router-dom'
import ErrorPage from './errorPage.jsx'
import App from './App.jsx'
import { Main } from './body'

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
        element: <h1>This is a the best shirt in town</h1>
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
