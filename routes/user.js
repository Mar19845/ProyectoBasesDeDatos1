var express = require('express');
var router = express.Router();
var bcrypt = require('bcrypt');
var pool = require('../db/db');
/*const { config } = require('dotenv/types');*/

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
    let adminDb;

    await pool.query("select usuario,password, administrador from usuarios where usuario=$1", [user],
        function (err, result) {
            if (err) throw err;
            if (result) {
                /*
                res.send(JSON.stringify({
                    "result": result.rows[0]
                }))*/
                userdb = result.rows[0].usuario
                passDb = result.rows[0].password
                adminDb = result.rows[0].administrador

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

router.post('/subscribe', async function (req, res) {
    let subs = req.body.subscripcion;

    console.log(user.post("/login"));
    await pool.query("UPDATE usuario SET subscripcion='true' WHERE nombre == $1", [user.post("/login")],
        function (err, result) {
            if (err) throw err;
            if (result) {
                res.setHeader("content-type", "application/json")
                res.send(JSON.stringify(result.rows));
                console.log("el query se envio con exito")
            }

            if (subs === "false") {
                req.session.subscripcion = "true";
                res.send(JSON.stringify({
                    "result": true,
                    "user": user,
                    "motivo": "",

                }))
            }
        })
})


module.exports = router;