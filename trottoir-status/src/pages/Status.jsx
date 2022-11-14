import React from 'react';
import ped from '../pedestrian.webp';
import lamp_on from '../street-light-lamp-4.jpg';
import lamp_off from '../street-light-lamp-photo-6.jpg';


const Status = () => {
    return (
        <div>
            <h1> Status</h1>
            <img src={ped} alt="un piéton marche"/>
            <img src={lamp_on} alt="lampadaire est allumé"/>
        </div>
    );
};

export default Status;