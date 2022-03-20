import React, { useState } from 'react'
import axios from 'axios';
const PersonForm = (props) => {
    const {people, setPeople} = props; //this is new
    const [firstName, setFirstName] = useState(""); 
    const [lastName, setLastName] = useState("");
    const onSubmitHandler = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/people', {
            firstName,    
            lastName   
        })
            .then(res=>{
                console.log(res); 
                console.log(res.data);
                // we will update the lifted state of our people array 
                //    to include the current value in state plus the single 
                //    new object created and returned from our post request. 
                setPeople([...people, res.data]); //this is new
            })
            .catch(err=>console.log(err))
    }       // **** Our return/form will remain unchanged!
    return (
        <form onSubmit={onSubmitHandler}>
            <p>
                <label>First Name</label><br/>
                <input type="text" onChange = {(e)=>setFirstName(e.target.value)}/>
            </p>
            <p>
                <label>Last Name</label><br/>
                <input type="text" onChange = {(e)=>setLastName(e.target.value)}/>
            </p>
            <input type="submit"/>
        </form>
    )
}
export default PersonForm;

