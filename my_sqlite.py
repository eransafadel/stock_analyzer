import sqlite3
from MyStock import MyStock

conn = sqlite3.connect('my_storage.db')  # create file if not exist else - connect to db

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE stocks (
#                 name text,
#                 sector text
#                 )""")
#cursor.execute("INSERT INTO stocks VALUES ('fb','Tech')")
ticker = input("please enter a tocker symbol")
stock = MyStock(ticker)
print(stock.name)
print(stock.sector)

cursor.execute("INSERT INTO stocks VALUES (:name,:sector)",(stock.ticker,stock.sector))

cursor.execute("SELECT * FROM stocks")
print(cursor.fetchall())
conn.commit()


conn.commit()
conn.close()
