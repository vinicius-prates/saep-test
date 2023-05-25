import {generate, parse, transform, stringify} from 'csv';
import sqlite3 from 'sqlite3';
import http from 'http';
import fs from 'fs';
import express from 'express';
import cors from 'cors';

const app = express();
app.use(cors());

const db = new sqlite3.Database('./db.sqlite');
const hostname = '127.0.0.1';
const port = 3000;

// const server = http.createServer((req, res) => {
//   res.statusCode = 200;
//   res.setHeader('Content-Type', 'text/plain');
//   res.end('Hello World');
// });

// server.listen(port, hostname, () => {
//   console.log(`Server running at http://${hostname}:${port}/`);
// });

app.get('/clientes', (req, res) => {
    console.log("caiu aqui")
    var sql = "select * from clientes";

    db.serialize(() => {
        db.all(sql, function(err, rows) {
          var jsondata = (JSON.stringify(rows));  
          //send a JSON response
          res.setHeader("Content-Type", "application/json; charset=UTF-8");
          res.writeHead(200);
          res.end(jsondata);
        //   db.close();
         });
    })
});

app.get('/concessionaria/:id', (req, res) => {
    // var sql = "select * from concessionarias inner join alocacao on concessionarias.id = alocacao.concessionaria where alocacao.automovel =" + req.params.id;
    var sql = "select alocacao.* ,  concessionarias.id , concessionarias.concessionaria as nome from concessionarias inner join alocacao on concessionarias.id = alocacao.concessionaria where alocacao.automovel = " + req.params.id

    db.serialize(() => {
        db.all(sql, function(err, rows) {
          var jsondata = (JSON.stringify(rows));  
          //send a JSON response
          res.setHeader("Content-Type", "application/json; charset=UTF-8");
          res.writeHead(200);
          res.end(jsondata);
        //   db.close();
         });
    })
});


app.get('/alocacao', (req, res) => {
    console.log("caiu aqui")
    var sql = "select area, sum(quantidade) as qtd from alocacao group by area  ";

    db.serialize(() => {
        db.all(sql, function(err, rows) {
          var jsondata = (JSON.stringify(rows));  
          //send a JSON response
          res.setHeader("Content-Type", "application/json; charset=UTF-8");
          res.writeHead(200);
          res.end(jsondata);
        //   db.close();
         });
    })
});

app.get('/alocacao/:id', (req, res) => {
    var sql = "select * from alocacao inner join automoveis on alocacao.automovel = automoveis.id where alocacao.area = " + req.params.id;
    // var dados = [req.params.id]

    db.serialize(() => {
        db.all(sql, function(err, rows) {
          var jsondata = (JSON.stringify(rows));  
          //send a JSON response
          res.setHeader("Content-Type", "application/json; charset=UTF-8");
          res.writeHead(200);
          res.end(jsondata);
        //   db.close();
         });
    })
});



app.get('/automoveis', (req, res) => {
    console.log("caiu aqui")
    var sql = "SELECT * from Automoveis";

    db.serialize(() => {
        db.all(sql, function(err, rows) {
          var jsondata = (JSON.stringify(rows));  
          //send a JSON response
          res.setHeader("Content-Type", "application/json; charset=UTF-8");
          res.writeHead(200);
          res.end(jsondata);
        //   db.close();
         });
    })
});

app.get('/automovel/:id', (req, res) => {
    var sql = "SELECT * FROM automoveis where id = " + req.params.id;
    db.serialize(() => {
        db.all(sql, function(err, rows) {
          var jsondata = (JSON.stringify(rows));  
          //send a JSON response
          res.setHeader("Content-Type", "application/json; charset=UTF-8");
          res.writeHead(200);
          res.end(jsondata);
        //   db.close();
         });
    })
})
app.post('/automovel/:id', (req, res) => {
    // var sql = "SELECT * FROM automoveis where id = " + req.params.id;
    var dados = [req.params.id]
    var sql = `UPDATE Alocacao  set quantidade = quantidade -1 where automovel = ? `;
    db.run(sql, dados, (err) =>{
        if (err){
            res.statusCode = 401
            return console.log(err.message)
        }
        res.statusCode = 200
    })

    db.close()
    res.send("Finalizado")
})


const retornaAutomoveis = () => {

}

const importar = () => {
    fs.createReadStream("./dados/automoveis.csv")
    .pipe(parse({ delimiter: ";", from_line: 2 }))
    .on("data", function (row) {
        db.serialize(function () {
            db.run(
            `INSERT INTO Automoveis VALUES (null, ?, ?)`,
            [row[1], row[2]],
            function (error) {
                if (error) {
                return console.log(error.message);
                }
                console.log(`Inserted a row with the id: ${this.lastID}`);
            }
            );
        });
        // console.log(row);
        // console.log(row[1]);
    })
    // db.close();
}

app.set('port', process.env.PORT || 5000);
app.listen(app.get('port'), () => {
  console.log('rodando na porta ', app.get('port'));
})

