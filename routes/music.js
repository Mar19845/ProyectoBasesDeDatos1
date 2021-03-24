var express = require('express');
var router = express.Router();
var bcrypt = require('bcrypt');
var pool = require('../db/db');

//entry point para devolver todas las canciones en la base de datos
router.get('/getSong', async function (req, res, next) {
    results = await pool.query("select cancion,album,artista,link_ from canciones");
    res.setHeader("content-type", "application/json")
    res.send(JSON.stringify(results.rows));
    console.log("Se ha enviado todo ")

})
//entry point para buscar una cancion 
router.post('/getSong', async function (req, res) {
    let cancion = req.body.cancion;
    await pool.query("select cancion,album,artista,link_ from canciones where cancion  ilike $1" , [ '%' + cancion + '%' ],
        function (err, result) {
            if (err) throw err;
            if (result) {
                res.setHeader("content-type", "application/json")
                res.send(JSON.stringify(result.rows));
                console.log("el query se envio con exito")
            }
        })
})
//entry point para buscar un album
router.post('/getAlbum', async function (req, res) {
    let album = req.body.album;
    await pool.query("select nombre,artista,genero from albumes where nombre  ilike $1" , [ '%' + album + '%' ],
        function (err, result) {
            if (err) throw err;
            if (result) {
                res.setHeader("content-type", "application/json")
                res.send(JSON.stringify(result.rows));
                console.log("el album ha sido enviado ")
            }
        })
})
//entry point para buscar por artistas
router.post('/getArtista', async function (req, res) {
    let nombre = req.body.nombre;
    await pool.query("select nombre from artistas where nombre  ilike $1" , [ '%' + nombre + '%' ],
        function (err, result) {
            if (err) throw err;
            if (result) {
                res.setHeader("content-type", "application/json")
                res.send(JSON.stringify(result.rows));
                console.log("el artista ha sido enviado ")
            }
        })
})
module.exports = router;