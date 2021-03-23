async function Login(user, password) {
   
    let result =  await fetch("http://localhost:8080/login", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "user": user,
            "password": password
        })
        
    })
    result = await result.json();
    
    
    

    //let user1 = result.result.usuario
    console.log(result.result)

    if (result.result === true) {
        alert("Login correcto");
    }
    else if(result.result === false) {
        alert(result.motivo);
    }    
   
    

}
function LoginUser() {
    const password = document.getElementById("input2").value;
    const user = document.getElementById("input1").value

    let passcheck= false;
    let usercheck= false;


    // si no ingreso un nombre de usuario, alertar que ingrese uno
    if(!user){
        usercheck= false;
        alert("Ingrese un nombre de Ususario");
    }
    else if(user.trim().length>0){
        usercheck= true;
    }
    //si no ingreso una contraseña se alerta al ususario
    if (!password) {
        alert("Ingrese una contraseña");
        passcheck= false
    }
    else if(password.trim().length>0){
        passcheck= true;
    }
    //si usercheck y passcheck son true, se hace el registro en la base de datos y se borran los datos 
    if(usercheck && passcheck){
        Login(user, password)
        document.getElementById("input2").value="";
        document.getElementById("input1").value="";
    }
}

const btn = document.getElementById("btn");
btn.addEventListener("click", LoginUser);
