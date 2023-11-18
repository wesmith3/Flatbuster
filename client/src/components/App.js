import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Header from "./Header";
import Footer from "./Footer";
import MenuBar from "./MenuBar";
import MovieCollection from './MovieCollection'
import Welcome from "./Welcome";

function App() {


  return (
  <div>
    <Header />
    <MenuBar />
    <Welcome />
    {/* <MovieCollection /> */}
    <Footer />
  </div>
  )
}

export default App;
