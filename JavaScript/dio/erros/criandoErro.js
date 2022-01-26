// new Error(message, fileName, lineNumber)

const meuErro = new Error('Mensagem inválida');
meuErro.name = "invalidMessage"

throw meuErro