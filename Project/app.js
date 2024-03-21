'use strict'

const makeGetRequestAndOutputData = (url)=>{

  const data = new FormData(document.querySelector('.formLogin'))

  fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data
    })
      .then(response => response.json())
      .then(data => {console.log(data)})
    
}


function main(){

    const form = document.querySelector(".formLogin").addEventListener('submit', (event) =>{
        
        event.preventDefault();

        makeGetRequestAndOutputData('http://127.0.0.1:8000/user/login/');

    })
}

main();