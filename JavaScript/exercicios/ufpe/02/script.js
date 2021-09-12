function ler(){
    let num = window.document.getElementById('num')
    let res = window.document.getElementById('res')
    let n = Number(num.value)

    if (n%2 == 0){
        ret = n ** 2    
    } else {
        ret = n * 5
    }

    res.innerText = `${ret}`
}