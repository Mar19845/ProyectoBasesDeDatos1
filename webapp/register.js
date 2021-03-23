//funcion asincrona para hacer un post en la base de datos
//comentario nuevo
async function register(user, password) {

    let result = await fetch("http://localhost:8080/post/newuser", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "user": user,
            "password": password
        })
    })
    result = await result.json();
    console.log(result);
    alert(result.result);
    //if (!result.success) alert("FAILED! ")
}

function checkPassword() {
    // variables para comprobar que todos los datos estan correctos
    let passcheck= false;
    let usercheck= false;
    // caraibles para almacenar los datos ingresados por el usuario
    const password2 = document.getElementById("input3").value;
    const password = document.getElementById("input2").value;
    const user = document.getElementById("input1").value

    //si el ususario ingreso un nombre correcto y no existe en la base de datos se devuele un true
    if(user){
        usercheck= true;
    }
    // si no ingreso un nombre de usuario, alertar que ingrese uno
    else if(!user){
        usercheck= false;
        alert("Ingrese un nombre de Ususario");
    }
    //si no ingreso una contraseña se alerta al ususario
    if (!password) {
        alert("Ingrese una contraseña");
        passcheck= false
    }
    //si ambas contraseñas no son iguales, se cambian el estado de la variable passcheck
    if(password!==password2){
        alert("La contraseñas no son iguales");
        document.getElementById("input3").value="";
        passcheck= false
    }
    //si ambas contraseñas son iguales, se cambian el estado de la variable passcheck
    else if (password===password2){
        passcheck= true
        
    }
    //si usercheck y passcheck son true, se hace el registro en la base de datos y se borran los datos 
    if(usercheck && passcheck){
        register(user, password)
        document.getElementById("input2").value="";
        document.getElementById("input1").value="";
        document.getElementById("input3").value="";
    }
}

const btn = document.getElementById("btn");
btn.addEventListener("click", checkPassword);



