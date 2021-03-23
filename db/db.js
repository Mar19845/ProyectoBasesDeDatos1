//conecion a postgresql
const { Pool } = require('pg')

//dot env para el manejo de links
require('dotenv').config()
//link para conectarse a la base de datos en el servidor
const connectionString = process.env.URL

const pool = new Pool({
  connectionString,
})

module.exports = pool;