function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

var input = document.getElementById("Asearch");
const url = "http://localhost:8080/get";
const song = document.getElementById("rolas");

input.addEventListener("keyup", function (event) {

  if (event.keyCode === 13) {

    readTodos();
    async function readTodos() {
      try {
        const result = await fetch(url, { method: "GET" })
        const todos = await result.json();
        console.log(todos);
        todos.forEach(t => {
            const li = document.createElement("li")
            li.textContent = t.name;
            li.id = t.ID;

            song.appendChild(li);
        })
        
    }
    catch (e) {
        console.log("Error reading the todos.")
    }

    }
  }
});