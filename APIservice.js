export default class APIService{
    // Insert an article
    static async getData(body){

        const response = await fetch(`http://localhost:5000/modify`,{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify(body)
    })
    
    const result = await response.json()

    return result.modified_data
    }

}