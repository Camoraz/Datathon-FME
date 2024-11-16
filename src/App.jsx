import { useState } from 'react'
import APIService from '../APIservice'
import './App.css'

function App() {
  const [data, setData] = useState({'name':'Raul', 'age':'legal', 'year':3})
  const [message, setMessage] = useState('')

  const sendData = () => {
    APIService.getData(data)
    .then((response) => setMessage(response))
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    sendData()
  }
  return (
    <>
      <h1>Perfect Groups Generator AI powered blockchain ML</h1>
      <button onClick={handleSubmit}>Click to return data</button>
      <form onSubmit={handleSubmit}>
        <label htmlFor=""></label>
        <input type="" />
      </form>
      {message && <p>{message}</p> }
    </>
  )
}

export default App
