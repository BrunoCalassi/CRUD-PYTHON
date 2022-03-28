from sqlite3 import Cursor
import pymysql

conexao = pymysql.connect(host="localhost", port=3306, database="teste1",user="root",password="root",autocommit=True)


cursor = conexao.cursor()

#CREATE 
try:
    cursor.execute("INSERT INTO cliente (nome) values ('Maria')")
except Exception as e:
    print(f"Erro: {e}")

#UPDATE
try:
    cursor.execute("UPDATE cliente SET nome='Jessica' where id= 2")
except Exception as e:
    print(f"Erro: {e}")

#DELETE 
try:
    cursor.execute("DELETE FROM cliente where id= 3")
except Exception as e:
    print(f"Erro: {e}")

#READ
try:
    cursor.execute("SELECT * FROM cliente")
    print(cursor.fetchall())
    # for row in cursor.fetchall():
        #print(row)
except Exception as e:
    print(f"Erro: {e}")




conexao.close()