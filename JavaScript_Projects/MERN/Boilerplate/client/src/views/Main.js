import React, { useState } from 'react'
import axios from 'axios';
import PersonForm from '../components/PersonForm';
import PersonList from '../components/PersonList';
const Main = (props) => {
    //Establish lifted state to have access to getter and setter in other components
    const [people, setPeople] = useState([]);
    
    return (
        <div>
    	{/* PersonForm and Person List can both utilize the getter and setter established in their parent component:  */}
           <PersonForm people={people} setPeople={setPeople} />
           <hr/>
           <PersonList people={people} setPeople={setPeople} />
        </div>
    )
}
export default Main;
