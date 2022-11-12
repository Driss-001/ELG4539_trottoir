import logo from './logo.svg';
import './App.css';
import * as React from 'react';
import { Box } from '@mui/material/Box';
import Button from '@mui/material/Button'
import Toolbar from '@mui/material/Toolbar';
import { makeStyles ,ThemeProvider , createTheme, SvgIcon, StepIcon, ListItemIcon, ListItemSecondaryAction } from '@mui/material';
import { Typography } from '@mui/material/styles/createTypography';
import AppBar from '@mui/material/AppBar';
import Container from '@mui/material/Container';
import TextField from '@mui/material';
import IconButton from '@mui/material/IconButton';
import MenuItem from '@mui/material/MenuItem';
import {Menu} from '@mui/material/Menu';
import SwipeableDrawer from '@mui/material/SwipeableDrawer';
import Drawer from '@mui/material/Drawer';
import AccessibilityRoundedIcon from '@mui/icons-material/AccessibilityRounded';
import NordicWalkingIcon from '@mui/icons-material/NordicWalking';
const drawerWidth = 240;


const Mytheme = createTheme({
  palette:{
    primary:{
      light:"#d9e4ec",
      main:"#b7cfdc",
      dark:"6aabc2",
      contrastText:"385e72"
    },
    secondary:{
      light:"#bdc6d9",
      main:"#52688f",
      dark:"e3e7f1",
      contrastText:"7391c8"      
    }
  }
})

function App() {
  return (
  <ThemeProvider theme={Mytheme}>
    <div className="App">
      <AppBar
      position='static'
      color='primary'
      style={{ borderRadius:"80px"}}>
        <IconButton color='inherit'>
          <ListItemSecondaryAction/>
        </IconButton>

      </AppBar>
      <header className="App-header">
        <AppBar  position='static'
        title ="ELG4539: Statut du trottoir">
        </AppBar>

        <img src={logo} className="App-logo" alt="logo" />


      </header>
    </div>
  </ThemeProvider>  
  );
}

export default App;
