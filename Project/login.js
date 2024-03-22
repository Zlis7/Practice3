"use strict"

const urlLogin = "http://127.0.0.1:8000/user/login/";

const NameClassForm = "formLogin"

const nameInputEmail = "email";
const nameInputPassword = "password";

const getFormData = () =>{
  return new FormData(document.querySelector("." + NameClassForm));
}

const FormDataInJson = (formData) => {
  return {
    [nameInputEmail]: formData.get(nameInputEmail),
    [nameInputPassword]: formData.get(nameInputPassword)
  }
}

const sendRequestLogin = () =>{
  const formData = getFormData();
  
  fetch(urlLogin, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(FormDataInJson(formData))
  })
    .then(response => response.json())
    .then(data => {
      console.log(data)
  })

}

function main(){
    const form = document.querySelector("." + NameClassForm).addEventListener("submit", (event) =>{
        
      event.preventDefault();
      sendRequestLogin();
    })
}

main();