const express = require("express")
const app = express();
//cors, permite que se puedan hacer get/post desde cualquier pagina
var cors = require('cors')
app.use(express.json(), cors())


//dot env para el manejo de links
require('dotenv').config()
//link para conectarse a la base de datos en el servidor
const connectionString = process.env.URL


//conecion a postgresql
const { Pool } = require('pg')

const pool = new Pool({
  connectionString,
})

//si entran al local host se desplega la pagina, index http://localhost:8080/
app.get("/", (req, res) => res.sendFile(`${__dirname}/index.html`))
//un entry point del servidor
app.get("/get", async (req, res) => {
  const rows = await readTodos();
  console.log("el get funciona")
  res.setHeader("content-type", "application/json")
  res.send(JSON.stringify(rows))
})
// pone al servidor a esuchar en el puerto 8080
app.listen(8080, () => console.log("Web server is listening.. on port 8080"))

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