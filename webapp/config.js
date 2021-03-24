var btnAbrirPopup = document.getElementById('artista'),
	overlay = document.getElementById('overlay'),
	popup = document.getElementById('popup'),
	btnCerrarPopup = document.getElementById('btn-cerrar-popup')
    btnAbrirPopup2 = document.getElementById('manager');

btnAbrirPopup.addEventListener('click', function(){
	overlay.classList.add('active');
	popup.classList.add('active');
});

btnCerrarPopup.addEventListener('click', function(e){
	e.preventDefault();
	overlay.classList.remove('active');
	popup.classList.remove('active');
});

btnAbrirPopup2.addEventListener('click', function(){
	overlay3.classList.add('active');
	popup3.classList.add('active');
});


inactivar = document.getElementById("btnI");
modificar = document.getElementById("btnM");
eliminar = document.getElementById("btnE");
overlay2 = document.getElementById("overlay2");
overlay3 = document.getElementById("overlay3");

inactivar.addEventListener('click', function(){
    overlay2.classList.add('active');
	popup2.classList.add('active');
});

modificar.addEventListener('click', function(){
    overlay2.classList.add('active');
	popup2.classList.add('active');
});

eliminar.addEventListener('click', function(){
    overlay2.classList.add('active');
	popup2.classList.add('active');
});

btnCerrarPopup.addEventListener('click', function(e){
	e.preventDefault();
	overlay2.classList.remove('active');
	popup2.classList.remove('active');
});

btnCerrarPopup.addEventListener('click', function(e){
	e.preventDefault();
	overlay3.classList.remove('active');
	popup3.classList.remove('active');
});

crearCancion = document.getElementById("Crear_C")
crearCancion.addEventListener('click', function(){
    overlay4.classList.add('active');
	popup4.classList.add('active');
});


const boton = document.getElementById("subs");
// funcion que hace un post para subscribirse
async function Subscribe(subscripcion) {
   
    let result =  await fetch("http://localhost:8080/subcribirse", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "subscripcion": subscripcion
        })
        
    })
    result = await result.json();
    //si la respuesta es true, es decir subscribio al usuario, devuelve un mensaje
    if (result.result === "true") {
        alert(result.mensaje);
        
            
    }
    //si la respuesta es false, es decir le quito la subscripcion al usuario, devuelve un mensaje
    else if(result.result === "false") {
        alert(result.mensaje);
        
    }    
}
//funcion que consigue el estado de subscripcion del usuari0
async function GetSub(){
    const result = await fetch("http://localhost:8080/subcribirse/check", { method: "GET" });
    const estado = await result.json();
    const subUser=estado[0].suscripcion
    if(subUser===true){
        alert("Se procedera a cancelar su Subscripcion")
        Subscribe("false")
    }
    else if(subUser===false){
        alert("Se procedera a realizar su subscripcion")
        Subscribe("true")
    }
}
//funcion que llama la funcion anterior
function actSub(){
    GetSub()
}

boton.addEventListener("click",actSub);


ActivateAdmin()
//funcion que activa botones del admin
function ActivateAdmin(){
    getAdmin()
}
//funcion que verifica si un usuario es admin o no
async function getAdmin(){
    const result = await fetch("http://localhost:8080/admin/check", { method: "GET" });
    const estado = await result.json();
    const adminUser=estado[0].administrador
    if(adminUser===true){
        document.getElementById("btnI").disabled = false;
        document.getElementById("btnM").disabled = false;
        document.getElementById("btnE").disabled = false;
    }
    else if(adminUser===false){
        document.getElementById("btnI").disabled = true;
        document.getElementById("btnM").disabled = true;
        document.getElementById("btnE").disabled = true;
    }
}

const botonArtista =  document.getElementById("btnArtista");

boton.addEventListener("click",getNewArtista);
async function getNewArtista(){
    const Artista =  document.getElementById("NombreArtista").value;
    let result =  await fetch("http://localhost:8080/", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "artista": Artista
        })
        
    })
}
