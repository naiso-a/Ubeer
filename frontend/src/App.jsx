import React from "react";
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Home from "./components/Home";
import Navbar from "./components/Navbar";
import Brewery from "./components/Brewery/Brewery";

function App() {
  return (
    <div className='App'>
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/Brewery' element={<Brewery />} />
        </Routes>
      </Router>
      
    </div>
  );
}

export default App;
