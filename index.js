const url = "http://localhost:8080/get";
let userDb= [];
let userPsDb= [];
console.log("este es uno global");
function Login() {
    console.log("afuera de los for");
    const user = document.getElementById('input1').value;
    const pass = document.getElementById('input2').value;
    getFromUserDatabase();
    for(let i = 0;i<userDb;i++){
        for (let j =0;j<userPsDb;j++){
            if(user==userDb[i]){
                alert("Esta mierda Funciono!!!!!!!!");
                console.log("Esta mierda Funciono!!!!!!!!");
            }
            else{
                console.log("no funciona");
            }
        }
    }

}



async function getFromUserDatabase() {
    try {
        const result = await fetch(url, { method: "GET" })
        const user = await result.json();
        user.forEach(t => {
            userDb.push(t.usuario);
            userPsDb.push(t.password);
        })

    }
    catch (e) {
        console.log("Error reading the todos.")
    }

}