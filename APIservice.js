export default class APIService{
    // Insert an article
    static async getData(body){

        const response = await fetch(`http://127.0.0.1:5000/api`,{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
      },
      
      body:JSON.stringify(body)
    })

    const result = await response.json()
    return result.data
    }

}