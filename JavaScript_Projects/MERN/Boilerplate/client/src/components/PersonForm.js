//imports packages dependencies
import React, { useEffect, useState } from 'react'
import axios from 'axios'; 
//save component to const 
const PersonForm= () => {
    //save key val pair of message, useState default message is "loading..."
    const [ message, setMessage ] = useState("Loading...")
    //useEffect makes call to api upon rendering
    useEffect(()=>{
        //axios makes request 
        axios.get("http://localhost:8000/api")
            //then save response from api as message from line 7
            .then(res=>setMessage(res.data.message))
            //if errors, log to console
            .catch(err=>console.log(err))
    }, []);
    //JSX to be rendered 
    return (
        <div>
            <h2>Message from the backend: {message}</h2>
        </div>
    )
}
//Export component
export default PersonForm;

