function valor(num){
    return Number(num.value)
}
function media() {
    let num1 = document.getElementById('num1')
    let num2 = document.getElementById('num2')
    let num3 = document.getElementById('num3')
    let res = document.querySelector('h2#res')

    let media = (valor(num1)+valor(num2)+valor(num3)) / 3
    res.innerHTML += `${media}`
}