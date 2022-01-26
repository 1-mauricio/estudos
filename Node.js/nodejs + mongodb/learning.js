const mongoose = require("mongoose");

// um banco é criado automaticamente se não existir
mongoose
    .connect("mongodb://localhost/teste")
    .then(() => {
        console.log("mongodb conectado");
    })
    .catch((e) => {
        console.log("houve um erro ao se conectar " + e);
    });

// Model - usuarios
// definindo o model
const UsuariosSchema = mongoose.Schema({
    nome: {
        type: String,
        require: true, // campo obrigatorio ou nao
    },
    sobrenome: {
        type: String,
        require: true,
    },
    email: {
        type: String,
        require: true,
    },
    idade: {
        type: Number,
        require: true,
    },
    pais: {
        type: String,
    },
});

// nome da collection/table
mongoose.model("usuarios", UsuariosSchema);

const novoUsuario = mongoose.model('usuarios')

new novoUsuario({
    nome: "Mauricio",
    sobrenome: "Alves",
    email: "email@email.com",
    idade: 20,
    pais: 'Brasil',
})
    .save()
    .then(() => {
        console.log("Usuário criado com sucesso");
    })
    .catch((e) => {
        console.log("houve um erro ao registrar o usuario" + e);
    });
