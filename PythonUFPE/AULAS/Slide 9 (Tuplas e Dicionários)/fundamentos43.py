tab = [(1000,'M'),(900,'CM'),(500,'D'), (400,'CD'), (100,'C'),
       (90,'XC'), (50,'L'), (40,'XL'), (10,'X'), (9,'IX'),
       (5,'V'), (4,'IV'), (1,'I')]

num = int(input('Digite um número: '))
while (num < 1) or (num > 3999) :
    num = int(input('Digite um número: '))

aux = num
res = ''

for i in range (len(tab)) : 
    while aux >= tab[i][0] :
        res = res + tab[i][1]
        aux = aux - tab[i][0]

print(num, '=', res)