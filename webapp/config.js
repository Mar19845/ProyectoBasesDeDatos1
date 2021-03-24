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
    overlay5.classList.add('active');
	popup5.classList.add('active');
});

eliminar.addEventListener('click', function(){
    overlay6.classList.add('active');
	popup6.classList.add('active');
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

//funcion que Crea un nuevo artista
const botonArtista =  document.getElementById("btnArtista");
botonArtista.addEventListener("click",CrearArtista);

const link = "";
function CrearArtista(){
    const Artista =  document.getElementById("NombreArtista").value;
    const Album = document.getElementById("AlbumArtista").value;
    const Cancion = document.getElementById("CancionArtista").value;
    const Link = document.getElementById("LinkCancion").value;

    getNewArtista(Artista)
    console.log("Esto es una asincore")
}

async function getNewArtista(Artista){
    let result =  await fetch("http://localhost:8080/artista/create", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "artista": Artista,
        })
        
    })
    result = await result.json();
    if (result.result === true) {
        alert("Felicidades, es un Artista");        
    }
}

//funcion crea un manager
const botonManager =  document.getElementById("btnManager");
botonManager.addEventListener("click",CrearManager);

function CrearManager(){
    const Manager =  document.getElementById("NombreManager").value;
    getNewManager(Manager)
    console.log("Esto es una asincore")
}
async function getNewManager(Manager){
    let result =  await fetch("http://localhost:8080/manager/create", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "manager": Manager
        })
        
    })
    result = await result.json();
    if (result.result === true) {
        alert("Felicidades, es un Manager");        
    }
}

//funcion inactivar cancion
const botonInactivar =  document.getElementById("Inactivar");
botonInactivar.addEventListener("click",InactivarCancion);

function InactivarCancion(){
    const Cancion =  document.getElementById("C_inactivar").value;
    getNewSong(Cancion)
    console.log("Esto es una asincore")
}
async function getNewSong(Cancion){
    let result =  await fetch("http://localhost:8080/inactivar/cancion", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "cancion": Cancion
        })
        
    })
    result = await result.json();
    if (result.result === true) {
        alert("Se ha inactivado la cancion");        
    }
}

//funcion modificar cancion
const botonModificar =  document.getElementById("Modificar");
botonModificar.addEventListener("click",ModificarCancion);

function ModificarCancion(){
    const Cancion =  document.getElementById("C_Modificar").value;
    const Link = document.getElementById("L_Modificar").value;
    getModiSong(Cancion, Link)
    console.log("Esto es una asincore")
}
async function getModiSong(Cancion, Link){
    let result =  await fetch("http://localhost:8080/modificar/cancion", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "cancion": Cancion,
            "link":Link
        })
        
    })
    result = await result.json();
    if (result.result === true) {
        alert("Se ha modificado la cancion");        
    }
}

//funcion eliminar cancion
const botonEliminar =  document.getElementById("Eliminar");
botonEliminar.addEventListener("click",EliminarCancion);

function EliminarCancion(){
    const Cancion =  document.getElementById("C_Eliminar").value;
    getElimSong(Cancion)
    console.log("Esto es una asincore")
}
async function getElimSong(Cancion){
    let result =  await fetch("http://localhost:8080/eliminar/cancion", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "cancion": Cancion
        })
        
    })
    result = await result.json();
    if (result.result === true) {
        alert("Se ha eliminado la cancion");        
    }
}
