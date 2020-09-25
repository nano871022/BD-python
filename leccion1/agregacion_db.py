import sqlite3

print(10*"#","Agregacion",10*"#")
class MySum:
  def __init__(self):
    self.count = 0
  def step(self, value):
    self.count += value
  def finalize(self):
    return self.count

con=sqlite3.connect(":memory:")
con.create_aggregate("mysum",1,MySum)

cursor=con.cursor()
cursor.execute("CREATE TABLE test(i)")

cursor.execute("INSERT INTO test(i) VALUES(1)")
cursor.execute("INSERT INTO test(i) VALUES(2)")

cursor.execute("SELECT mysum(i) from test")
print(cursor.fetchone()[0])
con.close()
print(30*"#")