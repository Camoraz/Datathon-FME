import React, { useState } from 'react';
import './App.css';
import APIService from '../APIservice';
import participants from '../data/datathon_participants.json'

function App() {
  const [data, setData] = useState({
    name: '',
    years: '',
    role: '',
    challenge: '',
    lang: '',
    availability: {'Saturday morning':false, 'Saturday afternoon':false , 'Saturday night': false, 'Sunday morning':false, "Sunday afternoon":false},
    level: '',
    age: '',
    hackathons: '',
    objective: ""
  });
  const [message, setMessage] = useState([]);
  const [selectedId, setSelectedId] = useState(null)
  const [res, setRes] = useState([])
  const updateMessage = (m) => {
    const newMessage = {...m}
    setRes(newMessage)
    const filteredData = participants.filter((item) => item.id in newMessage)
    console.log(filteredData)

    setMessage(filteredData)
  }
  
  const sendData = async () => {
    const dataCorrected = {...data, lang:data.lang.replaceAll(',', '').trim().split(' '), challenge: data.challenge.split(',')}
    const newMessage = await APIService.getData(dataCorrected);
    updateMessage(newMessage)
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setData({ ...data, [name]: value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    sendData();
  };

  const handleMulti = (event) =>  {
    console.log('clicked: ',event.target.value, 'previous: ',data.challenge)
    if (!data.challenge.includes(event.target.value)) {
      setData({ ...data, challenge: "".concat(data.challenge, ",", event.target.value)})
    } else 
      setData({ ...data, challenge: data.challenge.replace(event.target.value, '')})
  }

  const handleAvailability = (event) => 
  {
    const new_av = {...data.availability, [event.target.value]: !data.availability[event.target.value]}
    console.log("puta",new_av)

    setData({...data, availability: new_av})
    
  }

  const handleToggle = (id) => {
    setSelectedId((prevId) => (prevId === id ? null : id));
  };
  


  return (
    <>
      <h1 className='title'>Mao Finder 猫</h1>
      <div className={"wrapper"}>
      <form onSubmit={handleSubmit}>
        {/* Name */}
        <div className="inputDiv">
          <label>Nombre:</label>
          <input
            type="text"
            name="name"
            value={data.name}
            placeholder="Tu nombre"
            onChange={handleChange}
          />
        </div>

        {/* Years */}
        <div className="inputDiv">
          <label>Año de estudio:</label>
          <div className="buttonGroup">
            {['1st year', '2nd year', '3rd year', '4th year', 'Masters', 'PhD'].map((value) => (
              <button
                type="button"
                key={value}
                className={data.years === value ? 'radioButton active' : 'radioButton'}
                onClick={() => setData({ ...data, years: value })}
              >
                {value}
              </button>
            ))}
          </div>
        </div>

        {/* Role */}
        <div className="inputDiv">
          <label>Rol preferido:</label>
          <div className="buttonGroup">
            {['Analysis', 'Visualization', 'Development', 'Design'].map((value) => (
              <button
                type="button"
                key={value}
                className={data.role === value ? 'radioButton active' : 'radioButton'}
                onClick={() => setData({ ...data, role: value })}
              >
                {value}
              </button>
            ))}
          </div>
        </div>


        {/* Challenge */}
        <div className="inputDiv">
          <label>Desafío seleccionado:</label>
          <div className="buttonGroup">
            {['restb.ai challenge', 'aed challenge', 'mango challenge'].map((value) => (
              <button
                type="button"
                key={value}
                value={value}
                className={data.challenge.includes(value) ? 'radioButton active' : 'radioButton'}
                onClick={(event) => handleMulti(event)}
              >
                {value}
              </button>
            ))}
          </div>
        </div>

        {/* Languages */}
        <div className="inputDiv">
          <label>Idiomas preferidos:</label>
          <input
            type="text"
            name="lang"
            value={data.lang}
            placeholder="Español, Inglés, Catalán..."
            onChange={handleChange}
          />
        </div>

        {/* Availability */}
        <div className="inputDiv">
          <label>Disponibilidad:</label>
          {["Saturday morning", "Saturday afternoon", "Saturday night", "Sunday morning", "Sunday afternoon"].map((timeframe)=> (
            <button
              type='button'
              key={timeframe}
              className={data.availability[timeframe]? "radioButton active" : "radioButton"}
              value={timeframe}
              onClick={handleAvailability}
            >{timeframe}
            </button>
          ))}
          
        </div>

        {/* Level */}
        <div className="inputDiv">
          <label>Nivel de experiencia:</label>
          <div className="buttonGroup">
            {['Beginner', 'Intermediate', 'Advanced'].map((value) => (
              <button
                type="button"
                key={value}
                className={data.level === value ? 'radioButton active' : 'radioButton'}
                onClick={() => setData({ ...data, level: value })}
              >
                {value}
              </button>
            ))}
          </div>
        </div>

        {/* Age */}
        <div className="inputDiv">
          <label>Edad:</label>
          <input
            type="number"
            name="age"
            value={data.age}
            placeholder="Tu edad"
            onChange={handleChange}
          />
        </div>

        {/* Hackathons */}
        <div className="inputDiv">
          <label>Número de hackathons:</label>
          <input
            type="number"
            name="hackathons"
            value={data.hackathons}
            placeholder="0, 1, 2..."
            onChange={handleChange}
          />
        </div>
        {/* objective */}
        <div>
          <label>Objective</label>
          <input
          name = {"objective"}
          value={data.objective}
          placeholder="idk I just want to be loved" onChange={handleChange}></input>
        </div>
        <button type="submit">Enviar</button>
      </form>

      <div >
        {message && message.map((item) => (
          <ul key={item.id}>
            <button onClick={() => handleToggle(item.id)} className={"resultButton"}>
              <h2>{item.name} {res[item.id]}%</h2>
              </button> 
              {selectedId === item.id && (
                <div className={"textContainer"} >
                  <p>Age: {item.age}</p>
                  <p>Year: {item.year_of_study}</p>
                  <p>Level: {item.experience_level}</p>
                  
                  <p>Languages: {item.preferred_languages}</p>
                  <p >Objective: {item.objective}</p>
      
                </div>
              )}
          </ul>         
        ))
        }
      </div>
      </div>

    </>
    
  );
}
export default App;