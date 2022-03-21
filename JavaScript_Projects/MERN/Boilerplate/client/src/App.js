import React, { useState } from 'react';
import axios from 'axios';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Main from './views/Main';
import "./App.css";
const App = () => {

  return (
    <div className='App'>
      <BrowserRouter>
        <Routes>
          <Route element={<Main />} path="/" />
        </Routes>
      </BrowserRouter>
    </div>
  )
}
export default App;

