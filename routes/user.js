var express = require('express');
var router = express.Router();
var bcrypt = require('bcrypt');
var pool = require('../db/db');

//Handle POST request for User Registration
router.post('/post/newuser', async function (req, res, next) {

    let user = req.body.user;
    let password = req.body.password;
    let resultado = "Ususario creado con exito"
    // se usa bcrypt para hacer un hash de la contraseña del ususario
    var hashpassword = bcrypt.hashSync(req.body.password, 10);




    await pool.query("insert into Usuario values($1,$2,$3,$4,$5)", [user, password, "false", "", "false"],
        function (err, result) {
            if (err) throw err;
        })

    res.send(JSON.stringify({
        "result": resultado
    }))
    console.log("ususario creado con exito");
});

//Handle POST request for User Login
router.post('/login',async  function (req, res, next) {
    let user = req.body.user;
    let password = req.body.password;
    let resultado=false;
    
    await pool.query("select usuario,password from Usuario where usuario=$1", [user],
    function(err, result){
        if (err) throw err;
        if (result){
            res.send(JSON.stringify({
                "result": result.rows
            }))
        }

    });
});



module.exports = router;