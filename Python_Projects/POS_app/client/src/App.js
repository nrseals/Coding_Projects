import React, {useState, useEffect} from 'react';
import './App.css';

function App() {
  //useState to store data from backend
  const [data, setData] = useState({});
  // useEffect to make request to api, this will later use axios to querey db
  useEffect(() => {
    fetch("http://localhost:5000/items").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  return (
    <div className="App">
      { 
        (typeof data.gigs === 'undefined') ? (
        <p>Loading . . . </p>
      ) : (
        data.gigs.map((gig, i) => (
          <p key={i}>{gig}</p>
        ))
      )}

    </div>
  );
}

export default App;
