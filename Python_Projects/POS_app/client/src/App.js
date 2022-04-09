import React, {useState, useEffect} from 'react';
import './App.css';

function App() {
  //useState to store data from backend
  const [apiData, setApiData] = useState({});
  // useEffect to make request to api, this will later use axios to querey db
  useEffect(() => {
    fetch("http://localhost:5000/items").then(
      res => res.json()
    ).then(
      data => {
        setApiData(data)
      }
    ).catch(err=>console.log(err))
  }, [])
  return (
    <div className="App">
      { 
        (typeof apiData.gigs === 'undefined') ? (
        <p>Loading . . . </p>
      ) : (
        apiData.gigs.map((gig) => (
          <p>{gig}</p>
        ))
      )}

    </div>
  );
}

export default App;
