import sqlite3

class CurrencyManager(object):
  def __init__(self,database=None):
    if not database:
      database=':memory:'
    self.conection=sqlite3.connect(database)
    self.cursor=self.conection.cursor()
    self.defaultTable(database)
  
  def defaultTable(self,database):
    if database == ':memory:':
      query= """
    CREATE TABLE currency (
      ID text primary key ,
      name text NOT NULL,
      symbol text NOT NULL )
    """
      self.cursor.execute(query)
      self.conection.commit()

  def insert(self,obj):
    query="INSERT INTO currency VALUES ('{}','{}','{}')".format(obj.code,obj.name,obj.symbol)
    self.cursor.execute(query)
    self.conection.commit()