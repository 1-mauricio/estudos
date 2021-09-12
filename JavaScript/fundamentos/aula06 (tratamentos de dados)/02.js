var s = 'JavaScript'
console.log(s.length)
console.log(s.toUpperCase())

var n1 = 1545.5
n1.toFixed(2).replace('.', ',') // 2 casas decimais e trocar ponto por virgula
console.log(n1.toFixed(2).replace('.', ','))
console.log(n1.toLocaleString('pt-Br', {style: 'currency', currency: 'BRL'})) // formatar para o R$