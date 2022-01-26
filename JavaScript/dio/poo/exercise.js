class ContaBancaria {
    constructor(agencia, numero, tipo) {
        this.agencia = agencia;
        this.numero = numero;
        this.tipo = tipo;
        this.saldo = 0;
    }

    get saldo() {
        return this._saldo;
    }

    set saldo(valor) {
        this._saldo = valor;
    }

    sacar(valor) {
        if (valor > this._saldo) return "operação negada";
        this._saldo -= valor;

        return this._saldo;
    }

    depositar(valor) {
        this._saldo += valor;
        return this._saldo;
    }
}

class ContaCorrente extends ContaBancaria {
    constructor(agencia, numero, cartaoCredito) {
        super(agencia, numero);
        this.tipo = "corrente";
        this.cartaoCredito = cartaoCredito
    }

    get cartaoCredito() {
        return this._cartaoCredito
    }

    set cartaoCredito(valor) {
        this._cartaoCredito = valor
    }
}


class ContaPoupanca extends ContaBancaria {
    constructor(agencia, numero) {
        super(agencia, numero);
        this.tipo = "poupanca";
        
    }
}

class ContaUniversitaria extends ContaBancaria {
    constructor(agencia, numero) {
        super(agencia, numero);
        this.tipo = "universitaria";
        
    }

    sacar(valor) {
        if (valor>500) return 'operacao negada!'

        this._saldo -= valor
    }
}

const minhaConta = new ContaCorrente(1, 234, true)
console.log(minhaConta.depositar(1000))
console.log(minhaConta.sacar(700))

const contaPoup = new ContaPoupanca(1, 22)
const contaUni = new ContaUniversitaria(1, 22)