import React from 'react';
import no_one from '../empty-road.jpg';
import ped from '../pedestrian.webp';
import car from '../car-driving-animated-gif-2.gif'
import lamp_on from '../street-light-lamp-4.jpg';
import lamp_off from '../street-light-lamp-photo-6.jpg';
import vélo from '../bike-gif-5.gif';
import useWebSocket from 'react-use-websocket';
import { useState, useCallback } from "react";
import MyJson from "../state.json";


const socketUrl = 'wss://localhost:8000/ws/TrottoirState/';
    
 
function refreshPage() {
    window.location.reload(false);
  }

function randomNumber(min, max) { 
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.round(Math.random() * (max - min) + min);
} 

const road_state =[
    { value : 0,
      image : no_one,
      texte : "rien n'est là"      
    },
   {   value : 1,
       image : ped,
        texte: "Un piéton marche"
   },  
    {
        value :2,
        image :car ,
        texte: "une voiture est sur la route"
    },
    {
      value :3,
      image :vélo ,
      texte: "un vélo est sur la route"
  }

   ]
const lamp_state =[
    { value : 0,
        image : lamp_off,
        texte: "Le lampadaire est éteint"      
      },
     {   value : 1,
         image : lamp_on,
         texte: "Le lampadaire est allumé"
     }

]   


const rnd1 = MyJson.RoadState;
const rnd2 = MyJson.LampState;
const weight = MyJson['weigt(g)'];


const Status = () => {
    

    

    return (
        <>
   
            <h1> Status du trottoir, weight: {weight} g </h1>
            <div class="cards">
            <div class="card">
            {road_state.map((item)=> item.value === rnd1 ? (
            <div class = "info">
            <h3>{item.texte} </h3>
             <img src={item.image} alt=""/>
             </div>
             ):null
                )} 
              </div> 
              </div>
            <div class="cards">  
            <div class="card">        
                 {lamp_state.map((item)=> item.value === rnd2 ? (
            <div class = "info">
            <h3>{item.texte} </h3>
             <img src={item.image}  alt=""/>
             </div>
             ):null
                )}
            </div>
            </div>     
            <>{setTimeout(() => {
                    refreshPage()
                            }, 3000)}</>   
    </>
    );
};


export default Status;