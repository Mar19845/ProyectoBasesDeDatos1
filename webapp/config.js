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
	overlay.classList.add('active');
	popup.classList.add('active');
});

const boton = document.getElementById("subs");

async function Subscribe(subscripcion) {
   
    let result =  await fetch("http://localhost:8080/subscribe", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "subscripcion": subscripcion
        })
        
    })
    result = await result.json();

    //let user1 = result.result.usuario
    console.log(result.result)

    if (result.result === true) {
        alert("SUSCRITO");
            
    }
    else if(result.result === false) {
        alert(result.motivo);
    }    
}

function subcribirse(){
    Subscribe(user, subscripcion);

}


/*if (adminDb === "false"){
    const pagina = document.location("../config.html");
    const boton = pagina.getElementById("sub1");
    boton.disabled = false;
}
else {
    res.send(JSON.stringify({
        "result": false,
        "user": null,
        "motivo": "Los datos no son iguales"

    }))
}*/

boton.addEventListener("click", subscribirse);
