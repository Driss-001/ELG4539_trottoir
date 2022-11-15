import {React ,useState} from "react";
import BarChartIcon from '@mui/icons-material/BarChart';
import GitHubIcon from '@mui/icons-material/GitHub';
import QuestionMarkIcon from '@mui/icons-material/QuestionMark';
import LightbulbCircleIcon from '@mui/icons-material/LightbulbCircle';
import MonitorIcon from '@mui/icons-material/Monitor';
import {FaBars} from "react-icons/fa"
import { NavLink } from "react-router-dom";
import logo from '../logo.svg'


const Sidebar = ({children}) => { 

    function refreshPage() {
        window.location.reload(false);
      }

    const[isOpen,setIsopen] = useState(false);
    const toggle =() => setIsopen(!isOpen);
    const menuItem =[
    {
        path:"/",
        name:"Dashboard",
        icon:<MonitorIcon/>
    },
    {
        path:"/about",
        name:"About",
        icon:<QuestionMarkIcon/>
    },
    {
        path:"/status",
        name:"Status",
        icon:<LightbulbCircleIcon/>
    },
    {
        path:"/analyse",
        name:"Analyse",
        icon:<BarChartIcon/>
    }
    ]

    return(
            <div className="container">
                <div style ={{width: isOpen ? "200px":"50px"}} className="sidebar">
                    <div className="top_section">
                        <h1 style={{display: isOpen ? "block":"none"}} className="logo"><GitHubIcon/></h1>
                        <div  style={{marginLeft: isOpen ? "50px":"0px"}} className="bars">
                            <FaBars onClick={toggle}/>
                        </div>
                    </div>
                    {
                        menuItem.map((item,index)=>(
                            <NavLink to ={item.path} key={index} className="link" activateclassName = "active">
                                <div className="icon">{item.icon}</div>
                                <div style={{display: isOpen ? "block":"none"}} className="link_text">{item.name}</div>
                            </NavLink>
                        ))
                    }
                </div>
                <main>{children}
                <span className='empty-space'>{""}</span>
                <span className='empty-space'>{""}</span>
                <span className='empty-space'>{""}</span>
                <span className='empty-space'>{""}</span>
                <img src={logo} className="App-logo" alt="logo"/>
                </main>
                
                 <>{setTimeout(() => {
                    refreshPage()
                            }, 10000)}</>
            </div>
          
    );
   

};

export default Sidebar;

