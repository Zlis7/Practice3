"use strict"

const urlRegister = "http://127.0.0.1:8000/user/register/";

const NameClassForm = "formRegister"

const nameInputEmail = "email";
const nameInputPassword = "password";
const nameInputFirstName = "first_name";
const nameInputLastName = "last_name";

const getFormData = () =>{
  return new FormData(document.querySelector("." + NameClassForm));
}

const FormDataInJson = (formData) => {
  return {
    [nameInputEmail]: formData.get(nameInputEmail),
    [nameInputPassword]: formData.get(nameInputPassword),
    [nameInputFirstName]: formData.get(nameInputFirstName),
    [nameInputLastName]: formData.get(nameInputLastName)
  }
}

const sendRequestRegister = () =>{
  const formData = getFormData();
  
  fetch(urlRegister, {
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
      sendRequestRegister();
    })
}

main();