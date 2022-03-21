import React, { useState } from 'react'
import axios from 'axios';
const PersonForm = (props) => {
    //initialize state
    const {people, setPeople} = props; 
    const [firstName, setFirstName] = useState(""); 
    const [lastName, setLastName] = useState("");
    //submit handler
    const onSubmitHandler = (e) => {
        //prevent refresh
        e.preventDefault();
        //request to send form data to db
        axios.post('http://localhost:8000/api/people', {
            firstName,    
            lastName   
        })  
            //requirements for promise
            .then(res=>{
                //console log results to ensure successs
                console.log(res); 
                console.log(res.data);
                // we will update the lifted state of our people array 
                //    to include the current value in state plus the single 
                //    new object created and returned from our post request. 
                setPeople([...people, res.data]); 
            })
            .catch(err=>console.log(err))
    } 
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

