import React, { useState } from 'react';
import './App.css';
import APIService from '../APIservice';
function App() {
  const [data, setData] = useState({
    name: '',
    years: '',
    role: '',
    challenge: '',
    lang: '',
    availability: '',
    level: '',
    age: '',
    hackathons: '',
  });
  const [message, setMessage] = useState('');

  const sendData = () => {
    const dataCorrected = {...data, lang:data.lang.replaceAll(',', '').trim().split(' '), challenge: data.challenge.replaceAll(',', '').trim().split(' ')}
    console.log(dataCorrected)
    APIService.getData(dataCorrected);
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
    console.log(event.target.value)
    if (!data.challenge.includes(event.target.value)) {
      setData({ ...data, challenge: "".concat(data.challenge, " ", event.target.value)})
    } else 
      setData({ ...data, challenge: data.challenge.replace(event.target.value, '')})
  }

  return (
    <>
      <h1>Perfect Groups Generator AI powered blockchain ML</h1>
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
            {['1', '2', '3', '4', 'masters', 'phd'].map((value) => (
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
            {['analysis', 'visualization', 'development', 'design'].map((value) => (
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
            {['restb.ai', 'aed challenge', 'mango challenge'].map((value) => (
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
          <input
            type="text"
            name="availability"
            value={data.availability}
            placeholder="Horas disponibles"
            onChange={handleChange}
          />
        </div>

        {/* Level */}
        <div className="inputDiv">
          <label>Nivel de experiencia:</label>
          <div className="buttonGroup">
            {['beginner', 'intermediate', 'advanced'].map((value) => (
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

        <button type="submit">Enviar</button>
      </form>
      {message && <p>{message}</p>}
    </>
  );
}

export default App;
