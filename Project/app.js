'use strict'

const makeGetRequestAndGetData = async(url)=>{
    const response = fetch(url,{
        method: 'GET',
        headers: {'Access-Control-Allow-Origin': '*'},
        mode: 'no-cors'
    })
    return await response.json()
}


function main(){

    const form = document.querySelector(".formLogin").addEventListener('submit', async(event) =>{
        event.preventDefault();
        
        const data = await makeGetRequestAndGetData('http://127.0.0.1:8000/user/login/');

        console.log(data)
        
    })
}

(main)()