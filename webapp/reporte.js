const div = document.getElementById("reporte")
const a = document.getElementById("a")
const b = document.getElementById("b")
const c = document.getElementById("c")
const d = document.getElementById("d")
const e = document.getElementById("e")
<<<<<<< Updated upstream
//reporteA()
=======
<<<<<<< HEAD
reporteA()
=======
//reporteA()
>>>>>>> ac2cc9d4e989cabd4f01a629b056663d90fec921
>>>>>>> Stashed changes
async function reporteA() {
    try {
        const result = await fetch("http://localhost:8080/obtener/reporteA", { method: "GET" })
        const todos = await result.json();
        console.log(todos);
        todos.forEach(t => {
            const li = document.createElement("li")
            li.textContent = t.nombre;
            //li.id = t.ID;

            a.appendChild(li);
        })
        
    }
    catch (e) {
        console.log("Error reading the todos.")
    }
}
//reporteB()
async function reporteB() {
    try {
        const result = await fetch("http://localhost:8080/obtener/reporteB", { method: "GET" })
        const todos = await result.json();
        console.log(todos);
        todos.forEach(t => {
            const li = document.createElement("li")
            li.textContent = t.artista+" "+t.count;
            //li.id = t.ID;

            b.appendChild(li);
        })
        
    }
    catch (e) {
        console.log("Error reading the todos.")
    }
}
//reporteD()
async function reporteD() {
    try {
        const result = await fetch("http://localhost:8080/obtener/reporteD", { method: "GET" })
        const todos = await result.json();
        console.log(todos);
        todos.forEach(t => {
            const li = document.createElement("li")
            li.textContent = t.nombre+" "+t.count;
            //li.id = t.ID;

            d.appendChild(li);
        })
        
    }
    catch (e) {
        console.log("Error reading the todos.")
    }
}
reporteE()
async function reporteE() {
    try {
        const result = await fetch("http://localhost:8080/obtener/reporteE", { method: "GET" })
        const todos = await result.json();
        console.log(todos);
        todos.forEach(t => {
            const li = document.createElement("li")
            li.textContent = t.usuario+" "+t.logins;
            //li.id = t.ID;

            e.appendChild(li);
        })
        
    }
    catch (e) {
        console.log("Error reading the todos.")
    }
<<<<<<< Updated upstream
}
=======
<<<<<<< HEAD
}
=======
}
>>>>>>> ac2cc9d4e989cabd4f01a629b056663d90fec921
>>>>>>> Stashed changes
