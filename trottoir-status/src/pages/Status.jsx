import React from 'react';
import ped from '../pedestrian.webp';
import lamp_on from '../street-light-lamp-4.jpg';
import lamp_off from '../street-light-lamp-photo-6.jpg';



const Status = () => {
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