
import './App.css';
import * as React from 'react';
//import { createTheme } from '@mui/material';
//import GitHubIcon from '@mui/icons-material/GitHub';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Analyse from './pages/Analyse';
import Status from './pages/Status';
import About from './pages/About';





//const drawerWidth = 240;


//const Mytheme = createTheme({
//  palette:{
//    primary:{
//      light:"#d9e4ec",
//      main:"#b7cfdc",
//      dark:"6aabc2",
//      contrastText:"385e72"
//    },
//    secondary:{
//      light:"#bdc6d9",
//      main:"#52688f",
//     dark:"e3e7f1",
//      contrastText:"7391c8"      
//    }
//  }
//})

  //function My App() {
  //  return (
  //<ThemeProvider theme={Mytheme}>
  //    <Box sx={{flexFrow:1}}>
  //   <div className="App">
  //     <AppBar
  //    position='static'
  //  color='primary'
  //      style={{ borderRadius:"80px"}} >
  //<Toolbar>
  //   <IconButton color='inherit' size ="large" edge = "start" aria-label='menu' sx = {{mr:2}}>
  //        <GitHubIcon/>
  //       </IconButton>
  //    <Typography variant ="h6"
  //    component = "div" sx={{flexFrow:1}}>
  //     ELG 4539 Projet de Design  : Moniteur Intéractif 
  //  </Typography>
  //   </Toolbar>
  // </AppBar>
  // <header className="App-header">
  //  <AppBar  position='static'
  // title ="ELG4539: Statut du trottoir">
  //  </AppBar>
  //  <p>
  //  Système d'Illumination de Trottoir Sélectif (SITS) 
  //  </p>
        
       //  <img src={logo} className="App-logo" alt="logo" />


    //   </header>
    // </div>
    // </Box>
    //</ThemeProvider>  
    // );
    //};



const App = () => {

    return (
      <BrowserRouter>

      <Sidebar>
      <Routes>
        <Route path ="/"element = {<Dashboard/>}/>
        <Route path ="/dashboard"element = {<Dashboard/>}/>
        <Route path ="/analyse"element = {<Analyse/>}/>
        <Route path ="/status"element = {<Status/>}/>
        <Route path ="/about"element = {<About/>}/>
      </Routes>
      </Sidebar>
    </BrowserRouter>
  );
};

export default App;

