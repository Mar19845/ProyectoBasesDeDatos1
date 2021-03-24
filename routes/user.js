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
                    req.session.user = user;
                    superUsuario = user;
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
// subscribe al ususario al servicio premuim
router.post('/subcribirse', async function (req, res) {
    let subs = req.body.subscripcion;


    await pool.query("UPDATE usuarios SET suscripcion=$1 WHERE usuario = $2", [subs, superUsuario],
        function (err, result) {
            if (err) throw err;
            if (result) {
                if (subs === "false") {
                    res.setHeader("content-type", "application/json")
                    res.send(JSON.stringify({
                        "result": subs,
                        "mensaje": "Se a cancelado su subscripcion al sistema"
                    }));
                    console.log("se cancelo la subscripcion del usuario " + superUsuario)

                }
                else {
                    res.setHeader("content-type", "application/json")
                    res.send(JSON.stringify({
                        "result": subs,
                        "mensaje": "Se a subscrito al servico de musica premium"
                    }));
                    console.log("el query se envio con exito")
                }
            }
        })
})
// chequea que el usuario este subscrito
router.get('/subcribirse/check', async function (req, res, next) {
    results = await pool.query("select suscripcion from usuarios where usuario =$1",[superUsuario])
    res.send(JSON.stringify(results.rows));
    console.log("Se ha enviado todo ")

})

// chequea que el usuario sea admin
router.get('/admin/check', async function (req, res, next) {
    results = await pool.query("select administrador from usuarios where usuario =$1",[superUsuario])
    res.send(JSON.stringify(results.rows));
    console.log("Se ha enviado todo ")

})

//funcion que crea un artista
router.post('/admin/check', async function (req, res, next) {
    results = await pool.query("select administrador from usuarios where usuario =$1",[superUsuario])
    res.send(JSON.stringify(results.rows));
    console.log("Se ha enviado todo ")

})

module.exports = router;