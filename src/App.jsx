import Home from "./pages/Home";
import Qualification from "./pages/Qualification";
import Form from "./pages/Form";

import { Routes, Route } from "react-router";

const App = () => {

  return (
    <Routes>
      <Route path='/' element={<Home />} />
      <Route path="Qualification" element={<Qualification />} />
      <Route path="Contact" element={<Form/>} />
    </Routes>
  );
}

export default App;
