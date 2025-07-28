import react from "react"
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import Home from "./pages/Home"
import Login from "./pages/Login"
import Register from "./pages/Register"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"

function Logout(){
  localStorage.clear()             // Deletes all data stored in the browser's local storage (like your access and refresh tokens)
  return <Navigate to="/login" />  // Redirects the user to the /login page.
}

function RegisterAndLogout(){
  localStorage.clear()  
  return <Register />  
}


function App() {
  
  return (
    <BrowserRouter>
      <Routes>
        <Route 
          path="/"
          element ={
            <ProtectedRoute> {/* Protects the Home page → only shows if user is authenticated */}
              <Home />
            </ProtectedRoute>
          } 
        />
        <Route path="/login"element = {<Login />}/>
        <Route path="/register"element = {<RegisterAndLogout />}/>
        <Route path="/logout"element = {<Logout />}/>
        <Route path="*"element = {<NotFound />}/> {/* Handles unknown routes */}
      </Routes>
    </BrowserRouter>
  )
}

export default App // Export App so it can be used in main.jsx or index.js
