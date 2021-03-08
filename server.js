const express = require("express")
const app = express();
//cors, permite que se puedan hacer get/post desde cualquier pagina
var cors = require('cors')
app.use(express.json(),cors())

//conecion a postgresql
const { Pool } = require('pg')
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'Lab05',
  password: '1234',
  port: 5432,
})
//si entran al local host se desplega la pagina, index http://localhost:8080/
app.get("/", (req, res) => res.sendFile(`${__dirname}/index.html`))
//get del servidor
app.get("/get", async (req, res) => {
  const rows = await readTodos();
  console.log("el get funciona")
  //res.send("Esto funcionaaaaaaaaaaaaaaaaa perrrooooos")
  res.setHeader("content-type", "application/json")
  res.send(JSON.stringify(rows))
})
// pone al servidor a esuchar en el puerto 8080
app.listen(8080, () => console.log("Web server is listening.. on port 8080"))


async function readTodos() {
  try {
    const results = await pool.query("select * from carros");
    return results.rows;
  }
  catch (e) {
    return [];
  }
}