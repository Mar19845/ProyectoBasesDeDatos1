var express = require('express');
var router = express.Router();
var bcrypt = require('bcrypt');
var pool = require('../db/db');

var superUsuario;
//Handle POST request for User Registration
router.post('/post/newuser', async function (req, res, next) {

    let user = req.body.user;
    let password = req.body.password;
    let resultado = "Ususario creado con exito"
    // se usa bcrypt para hacer un hash de la contraseña del ususario
    var hashpassword = bcrypt.hashSync(req.body.password, 10);

    await pool.query("insert into usuarios values($1,$2,$3,$4,$5)", [user, password, "false", "false", "false"],
        function (err, result) {
            if (err) throw err;
        })

    res.send(JSON.stringify({
        "result": resultado
    }))
    console.log("ususario creado con exito");
});

//Handle POST request for User Login
router.post('/login', async function (req, res, next) {
    let user = req.body.user;
    let password = req.body.password;
    let userdb;
    let passDb;

    await pool.query("select usuario,password from usuarios where usuario=$1", [user],
        function (err, result) {
            if (err) throw err;
            if (result) {
                /*
                res.send(JSON.stringify({
                    "result": result.rows[0]
                }))*/
                userdb = result.rows[0].usuario
                passDb = result.rows[0].password

                if (userdb === user && passDb === password) {
                    req.session.user=user;
                    superUsuario=user;
                    console.log(req.session.user)
                    res.send(JSON.stringify({
                        "result": true,
                        "user": user,
                        "motivo": "",

                    }))
                }
                else {
                    res.send(JSON.stringify({
                        "result": false,
                        "user": null,
                        "motivo": "Los datos no son iguales"

                    }))
                }
            }

        });
});


module.exports = router;