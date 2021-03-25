function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
var a = document.createElement("a");
var input = document.getElementById("Asearch");
const url = "http://localhost:8080/getSong";
const song = document.getElementById("rolas");

input.addEventListener("keyup", function (event) {

  if (event.keyCode === 13) {
    const cancion = document.getElementById("Asearch").value;
    searchSong(cancion)
    //searchAlbum(cancion)
    //searchArtista(cancion)

  }
});
var cancionRepro = 0
Canciones();
//funcion que consigue todas las canciones en la base de datos y las imprime
async function Canciones() {

  try {
    const result = await fetch(url, { method: "GET" })
    const canciones = await result.json();

    canciones.forEach(t => {
      const li = document.createElement("li")
      li.textContent = t.cancion;
      li.id = t.id;

      song.appendChild(li);
      if (UserSub === "true") {
        document.getElementById(t.id).addEventListener('click', e => {
          a.href = t.link_;
          a.target = "_blank";
          a.innerHTML = t.cancion;
          barraRepro.appendChild(a);
          //barraRepro.innerHTML=t.link

        })
      }
      console.log(UserSub)

      if(UserSub==="false"){ 
        if(cancionRepro < 4){
          document.getElementById(t.id).addEventListener('click', e => {

            a.href = t.link_;
            a.target = "_blank";
            a.innerHTML = t.cancion;
            barraRepro.appendChild(a);
            //barraRepro.innerHTML=t.link
            cancionRepro= cancionRepro+1
          })  
        }else{
          alert("NO ERES USUARIO PREMIUM, REGRESA MAS TARDE")
        }
      }  
    })

  }
  catch (e) {
    console.log("Error reading the todos.")
  }

}

// funcion para buscar una cancion especifica
async function searchSong(cancion) {

  let result = await fetch(url, {
    method: "POST", headers: { "content-type": "application/json" },
    body: JSON.stringify({
      "cancion": cancion
    })

  })
  result = await result.json();
  console.log(result[0]);
  while (document.getElementById("rolas").firstChild) {
    document.getElementById("rolas").removeChild(document.getElementById("rolas").lastChild);
  }
  result.forEach(song => {
    const li1 = document.createElement("li")
    li1.id = song.id;
    li1.textContent = song.cancion;
    document.getElementById("rolas").appendChild(li1);
    //funcion que agrega el link a la barra de reproduccion y hacer un href a youtube
    document.getElementById(song.id).addEventListener('click', e => {

      a.href = song.link_;
      a.target = "_blank";
      a.innerHTML = song.cancion;
      barraRepro.appendChild(a);
      //barraRepro.innerHTML=t.link

    })
  })
}
//query para buscar un album especifico
async function searchAlbum(album) {

  let result = await fetch("http://localhost:8080/getAlbum", {
    method: "POST", headers: { "content-type": "application/json" },
    body: JSON.stringify({
      "album": album
    })

  })
  result = await result.json();
  console.log(result[0]);
  while (document.getElementById("rolas").firstChild) {
    document.getElementById("rolas").removeChild(document.getElementById("rolas").lastChild);
  }
  result.forEach(a => {
    const li1 = document.createElement("li")
    li1.id = a.nombre;
    li1.textContent = a.nombre;
    document.getElementById("rolas").appendChild(li1);
  })
}

//query para buscar un artista especifico
async function searchArtista(nombre) {

  let result = await fetch("http://localhost:8080/getArtista", {
    method: "POST", headers: { "content-type": "application/json" },
    body: JSON.stringify({
      "nombre": nombre
    })

  })
  result = await result.json();
  console.log(result[0]);
  while (document.getElementById("rolas").firstChild) {
    document.getElementById("rolas").removeChild(document.getElementById("rolas").lastChild);
  }
  result.forEach(a => {
    const li1 = document.createElement("li")
    li1.id = a.nombre
    li1.textContent = a.nombre;
    document.getElementById("rolas").appendChild(li1);
  })
}

let UserSub=false;
//busca si esta subscriot el usuario
//UserF()
function UserF(){
 GetSub() 

}
async function GetSub() {
  const result = await fetch("http://localhost:8080/subcribirse/check", { method: "GET" });
  const estado = await result.json();
  const subUser = estado[0].suscripcion
  if (subUser === true) {
    UserSub = subUser
    //alert("Se procedera a cancelar su Subscripcion")
    Subscribe("false")
  }
  else if (subUser === false) {
    alert("Se procedera a realizar su subscripcion")
    UserSub = subUser
    Subscribe("true")
  }
}
let barraRepro = document.getElementById("barras");
