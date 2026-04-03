import mysql.connector

# 🔧 CHANGE THESE VALUES
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # 🔥 put your MySQL password
    database="hospital"               # 🔥 your database name
)

cursor = conn.cursor()
