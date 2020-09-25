import sqlite3
print(10*"#","Rollback",10*"#")
con=sqlite3.connect(":memory:")
cursor=con.cursor()
cursor.execute("""
  CREATE TABLE currency(
    ID integer primary key AUTOINCREMENT,
    name text,
    symbol text
  )
""")
con.commit()

cursor.execute("INSERT INTO currency VALUES (1,'Peso (ARG)','$')")
cursor.execute("INSERT INTO currency VALUES (2,'Dolar (ARG)','U$S')")


con.rollback()
query="SELECT * FROM currency"

currencies=cursor.execute(query).fetchall()

print(currencies)

con.close()
print(30*"#")
