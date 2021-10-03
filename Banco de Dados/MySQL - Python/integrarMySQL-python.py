import mysql.connector


conexao = mysql.connector.connect(
    host='localhost', 
    user='root',
    database='PythonSQL')

print("Conexão bem sucedida")

cursor = conexao.cursor()

query = ("INSERT INTO vendas "
"(id_venda, cliente, produto, data_venda, preco, quantidade) "
" VALUES (2 , 'Maria', 'PC', '2020-12-15', 8005, 1)")

cursor.execute(query)
conexao.commit()

comando = ("SELECT id_venda, cliente, produto FROM vendas")

cursor.execute(comando)

for (id_venda, cliente, produto) in cursor:
    print(f"{id_venda} - {cliente} - {produto}")

cursor.close()
conexao.close()