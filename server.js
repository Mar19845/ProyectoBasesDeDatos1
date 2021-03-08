const express = require ("express")
const app = express();
app.use(express.json())

//conecion a postgresql
const { Pool } = require('pg')
const pool = new Pool({
    user: '{user}',
    host: '{host}',
    database: '{database}',
    password: '{password}',
    port: 5432,
  })

//get del servidor
app.get("/get", async (req, res) => {
    console.log("el get funciona")
    res.send("Esto funcionaaaaaaaaaaaaaaaaa perrrooooos")
})
// pone al servidor a esuchar en el puerto 8080
app.listen(8080, () => console.log("Web server is listening.. on port 8080"))

