"use strict"

const urlLogin = "http://127.0.0.1:8000/user/fileupload/";

const NameClassForm = "formFile"

const nameInputFile = "file";

const sendRequestFile = () =>{

    const data = new FormData(document.querySelector("." + NameClassForm)).get(nameInputFile)

    fetch(urlLogin, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .then(data => {
        onsole.log(data)
    })

}

function main(){
    const form = document.querySelector("." + NameClassForm).addEventListener("submit", (event) =>{
        
      event.preventDefault();
      sendRequestFile();
    })
}

main();