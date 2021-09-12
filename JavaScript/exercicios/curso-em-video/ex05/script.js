function number(num){
    return Number(num.value)
}

function contar(){
    var inicio = document.getElementById('inicio')
    var fim = document.getElementById('fim')
    var passo = document.getElementById('passo')
    var res = document.getElementById('res')

    console.log(inicio)

    if (inicio == '' || fim == '' || passo == ''){
        res.innerHTML = "Impossível contar"
    } else {
        res.innerHTML = "Contando: " 
        for(let c = number(inicio); c < number(fim); c + number(passo)){
            res.innerHTML += `${c}`
        }    
    }
}