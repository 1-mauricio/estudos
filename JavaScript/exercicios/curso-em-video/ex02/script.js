var msg = window.document.getElementById('msg')
var saud = document.getElementById('saudacao')
var data = new Date()
var hora = data.getHours()
msg.innerText = `Agora são ${hora} horas`
if (hora >= 0 && hora < 12) {
    document.body.style.background = '#e2cd9f'
    saud.innerHTML = 'Bom Dia'
} else if (hora>=12 && hora < 18) {
    document.body.style.background = '#b9846f'
    saud.innerHTML = 'Boa Tarde'
} else {
    document.body.style.background = '#515154'
    saud.innerHTML = 'Boa Noite'
}