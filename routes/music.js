var express = require('express');
var router = express.Router();
var bcrypt = require('bcrypt');
var pool = require('../db/db');

router.get('/getSong', async function (req, res, next) {
    results = await pool.query("select cancion,album,artista from canciones");
    res.setHeader("content-type", "application/json")
    res.send(JSON.stringify(results.rows));
    console.log("Se ha enviado todo ")

})
router.post('/getSong', async function (req, res) {
    let cancion = req.body.cancion;
    await pool.query("select cancion,album,artista from canciones where cancion  ilike $1" , [ '%' + cancion + '%' ],
        function (err, result) {
            if (err) throw err;
            if (result) {
                res.setHeader("content-type", "application/json")
                res.send(JSON.stringify(result.rows));
                console.log("el query se envio con exito")
            }
        })
})

module.exports = router;