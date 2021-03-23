function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

var input = document.getElementById("Asearch");
const url = "http://localhost:8080/getSong";
const song = document.getElementById("rolas");

input.addEventListener("keyup", function (event) {

  if (event.keyCode === 13) {
    const cancion = document.getElementById("Asearch").value;
    searchSong(cancion)
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
        li1.textContent = song.cancion + song.album;
        document.getElementById("rolas").appendChild(li1);
      })
    }
  }
});
Canciones();
async function Canciones() {

  try {
    const result = await fetch(url, { method: "GET" })
    const canciones = await result.json();
    console.log(typeof (canciones));
    canciones.forEach(t => {
      const li = document.createElement("li")
      li.textContent = t.cancion + t.album;
      //li.id = t.ID;

      song.appendChild(li);
    })

  }
  catch (e) {
    console.log("Error reading the todos.")
  }

}