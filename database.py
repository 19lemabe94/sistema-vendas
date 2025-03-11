import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ssword2018",
        database="vendas_db"
    )
