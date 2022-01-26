const Sequelize = require("sequelize");
const sequelize = new Sequelize(
    "postgres://kcwmdipe:yEdjEgfajX57y_atxYYI1dbSXZ2wTh5u@motty.db.elephantsql.com/kcwmdipe",
    { dialect: "postgres" }
);

module.exports = {
    Sequelize: Sequelize,
    sequelize: sequelize
}

sequelize.authenticate().then(() => {
    console.log("Conectado com sucesso")
}).catch((e) => console.log("Falha ao se conectar "+ e))





// gerando tabela no banco

//inserir dados no banco

/*
Postagem.create({
    titulo:"Um titulo qualquer",
    conteudo: "adfksjhasdkjfhadlkfjhsfkljdshfakj" 
})
*/

/*
const Usuario = sequelize.define('usuarios', {
    nome: {
        type: Sequelize.STRING
    },
    sobrenome: {
        type: Sequelize.STRING
    },
    idade: {
        type: Sequelize.INTEGER
    },
    email: {
        type: Sequelize.STRING
    }
})

//Usuario.sync({force: true})
/*
Usuario.create({
    nome: "Mauricio",
    sobrenome: "Alves",
    idade: 20,
    email: "exemplo@gmail.com"
})
*/