import sqlite3
import hashlib

print(10*"#","Funciones",10*"#")
def md5sum(t):
  return hashlib.md5(t).hexdigest()

con=sqlite3.connect(":memory:")
con.create_function("md5",1,md5sum)
cursor=con.cursor()
cursor.execute("SELECT md5(?)",(b"foo",))
print(cursor.fetchone()[0])
con.close()
print(30*"#")