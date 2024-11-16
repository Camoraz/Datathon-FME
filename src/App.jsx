import { useState } from 'react'
import APIService from '../APIservice'
import './App.css'

function App() {
  const [data, setData] = useState({'years':'', 'role':'', 'challenge':'', 'lang': '', 'availability':'', 'level':'', 'age':'', 'hackathons':''})
  const [message, setMessage] = useState('')

  const sendData = () => {
    APIService.getData(data)
    .then((response) => setMessage(response))
  }

  const handleChange = (event) => {
    if (event.target.type == 'radio') {
      console.log(event.target.value == 'radio', event.target.type)
    }

    const { name, value } = event.target
    setData({...data, [name]: value})
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    sendData()
  }
  return (
    <>
      <h1>Perfect Groups Generator AI powered blockchain ML </h1>
      <button onClick={handleSubmit}>Click to return data</button>
      <form onSubmit={handleSubmit}>
        <label htmlFor=""></label>
        <p>{" ".concat( data['name'], '   ' ,data['years'], '   ' ,data['role'], '   ' ,data['challenge'], '   ' ,data['lang'], '   ' ,data['availability'], '   ' ,data['level'], '   ' ,data['age'], '   ' ,data['hackathons'])}</p>
        <input placeholder='Name' name='name' value={data.name} onChange={handleChange} />
        <div className='inputDiv'>
          <label htmlFor="">Year of study: </label>
          <input type='radio' name='years' value={'1'} onChange={handleChange}/>
          <input type="radio" name="years" value={'2'} onChange={handleChange} />
          <input type="radio" name="years" value={'3'} onChange={handleChange} />
          <input type="radio" name="years" value={'4'} onChange={handleChange} />
          <input type="radio" name="years" value={'masters'} onChange={handleChange}/>
          <input type="radio" name="years" value={'phd'} onChange={handleChange} />
        </div>
        <div className='inputDiv'>
          <label>Preferred Role: </label>
          <input type='radio' name='role' value={'analysis'} onChange={handleChange}/>
          <input type='radio' name='role' value={'visualization'} onChange={handleChange}/>
          <input type='radio' name='role' value={'development'} onChange={handleChange}/>
          <input type="radio" name="role" value={'design'} onChange={handleChange}/>
        </div>
        <div className='inputDiv'>
          <label>Challenge selected: </label>
          <input type="radio" name="challenge" value={'restb.ai'} onChange={handleChange} />
          <input type="radio" name="challenge" value={'aed challenge'} onChange={handleChange}/>
          <input type="radio" name="challenge" value={'mango challenge'} onChange={handleChange}/>
        </div>
        <div className='inputDiv'>
          <label>Preferred Languages:  </label>
          <input placeholder='Spanish, English, Catalan' name='lang' value={data.lang} onChange={handleChange}/>
        </div>
        <div className='inputDiv'>
          <label>Availability:  </label>
          <input placeholder='idk, esto se cambia' name='availability' value={data.availability} onChange={handleChange}/>
        </div>
        <div className='inputDiv'>
          <label>Experience level:  </label>
          <input type="radio" name="level" value={'beginner'}  onChange={handleChange}/>
          <input type="radio" name="level" value={'intermediate'}  onChange={handleChange} />
          <input type="radio" name="level" value={'advanced'}  onChange={handleChange} />
        </div>
        <div className='inputDiv'>
          <label>Age:  </label>
          <input placeholder='Your age' name='age' value={data.age} onChange={handleChange}/>
        </div>
        <div className='inputDiv'>
          <label>N. of hackathons done</label>
          <input placeholder='1, 2, ...' name='hackathons' value={data.hackathons} onChange={handleChange}/>
        </div>
        <button type='submit'>Submit</button>
      </form>
      {message && <p>{message}</p> }
    </>
  )
}

export default App
