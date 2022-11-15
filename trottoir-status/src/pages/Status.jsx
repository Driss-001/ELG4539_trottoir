import React from 'react';
import no_one from '../empty-road.jpg';
import ped from '../pedestrian.webp';
import car from '../car-driving-animated-gif-2.gif'
import lamp_on from '../street-light-lamp-4.jpg';
import lamp_off from '../street-light-lamp-photo-6.jpg';





const Status = () => {
    
    function randomNumber(min, max) { 
        return Math.random() * (max - min) + min;
    } 
    
    const road_state =[
        { value : 0,
          image : <img src={no_one} width={400} height={400}  alt=""/>,
          texte : <figcaption>rien n'est là</figcaption>      
        },
       {   value : 1,
           image : <img src={ped} width={400} height={400}  alt=""/>,
            texte: <figcaption>Un piéton marche</figcaption>
       },  
        {
            value :2,
            image :<img src={car} width={400} height={400}  alt=""/> ,
            texte: <figcaption>une voiture est sur la route</figcaption>
        }
   
       ]
    const lamp_state =[
        { value : 0,
            image : <img src={lamp_off} width={400} height={400}  alt=""/>,
            texte: <figcaption>Le lampadaire est éteint</figcaption>      
          },
         {   value : 1,
             image : <img src={lamp_on} width={400} height={400}  alt=""/>,
             texte: <figcaption>Le lampadaire est allumé</figcaption>
         }

    ]   

    const Img_size = { width: "10px", height: "10px" } ;
    return (
        <div>
            <h1> Status du trottoir</h1>
            <span className='empty-space'>{""}</span>
            <figcaption>Un piéton marche</figcaption>
            <img src={ped} width={400} height={400}  alt=""/>
            <span className='empty-space'>{""}</span>
            <figcaption>Le lampadaire est allumé</figcaption>
            <img src={lamp_on} width={400} height={400} alt="lamp"/>
            
        </div>
    );
};

export default Status;