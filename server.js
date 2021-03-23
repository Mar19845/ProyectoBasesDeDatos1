const express = require("express")
const bcrypt = require('bcrypt');
const app = express();
var pool = require('./db/db');
var indexRouter = require('./routes/user');
//cors, permite que se puedan hacer get/post desde cualquier pagina
var cors = require('cors')
app.use(express.json(), cors())


//si entran al local host se desplega la pagina, index http://localhost:8080/
app.get("/", (req, res) => res.sendFile(`${__dirname}/webapp/index.html`))


app.use('/', indexRouter);



//un entry point del servidor
app.get("/get", async (req, res) => {
  const rows = await readTodos();
  res.setHeader("content-type", "application/json")
  res.send(JSON.stringify(rows))
})


//funcion que hace un querie
async function readTodos() {
  try {
    const results = await pool.query("select usuario,password from Usuario");
    return results.rows;
  }
  catch (e) {
    return [];
  }
}

// pone al servidor a esuchar en el puerto 8080
app.listen(8080, () => console.log("Web server is listening.. on port 8080"))