//import express from 'express'
const express = require("express");
const app = express();
const { engine } = require("express-handlebars");
const bodyParser = require("body-parser");
const Post = require("./models/Post");

// Config
//Template Engine
app.engine("handlebars", engine({ defaultLayout: "main" }));
app.set("view engine", "handlebars");

//body parser
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

//Conexao com banco de dados

// Rotas

app.get("/", (req, res) => {
    //retorna todos os posts dentro da tabela
    Post.findAll({ order: [["id", "DESC"]] }).then((posts) => {
        res.render("home", { posts: posts });
    });
});

app.get("/cad", (req, res) => {
    res.render("formulario");
});

app.post("/add", (req, res) => {
    const titulo = req.body.titulo;
    const conteudo = req.body.conteudo;

    Post.create({
        titulo: titulo,
        conteudo: conteudo,
    })
        .then(() => {
            res.redirect("/");
            //res.send('Post criado com sucesso')
        })
        .catch((e) => res.send("Houve um erro" + e));
});

app.get("/deletar/:id", (req, res) => {
    Post.destroy({ where: { id: req.params.id } })
        .then(() => {
            res.send("Postagem deletada com sucesso");
            

        })
        .catch((error) => {
            res.send("Essa postagem não existe");
        });
});

/*
app.get('/', (req, res) => {
    //enviando arquivos
    res.sendFile(__dirname + '/html/index.html')
})

app.get('/sobre', (req, res) => {
    res.sendFile(__dirname + "/html/sobre.html")
})

app.get('/ola/:nome/:cargo', (req, res) => {
    const nome = req.params.nome
    const cargo = req.params.cargo
    res.send(`<h1>Olá, ${nome}</h1>` + `<h2>Seu cargo é ${cargo}</h2>`)
})
*/

app.listen(8000, () => {
    console.log("servidor rodando na url http://localhost:8000");
});
