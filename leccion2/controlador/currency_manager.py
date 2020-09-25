import sqlite3
from leccion2.errores.error import *
from leccion2.constantes.constante import *

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

  def get(self, code):
    query="SELECT * FROM currency WHERE ID='{}'".format(code)
    self.cursor.execute(query)
    data=self.cursor.fetchone()
    if not data:
      raise CurrencyDoesNotExists("No existe la momeda de codig {}".format(code))
    return Currency(code=data[0],
         name=data[1], 
         symbol=data[2])

  def filter(self, **kwargs):
    code=kwargs.get("code")
    name=kwargs.get("name")
    symbol=kwargs.get("symbol")

    condition=" WHERE "
    and_and=False
    and_condition=False

    if code:
      condition += "ID='{}'".format(code)
      and_condition=True
      and_and=True
    if name:
      if and_and:
        condition += "AND "
      condition += "name='{}'".format(name)
      and_condition=True
      and_and=True
    if symbol:
      if and_and:
        condition += "AND "
      condition += "symbol='{}'".format(symbol)
      and_condition=True
      and_and=True
    query='SELECT * FROM currency'
    if and_condition:
      query += condition
    #print(query)
    self.cursor.execute(query)
    result=self.cursor.fetchall()

    currencies=[]
    for data in result:
      currency=Currency(code=data[0],
       name=data[1], 
       symbol=data[2])
      currencies.append(currency)
    return currencies
  
  def update(self,old_obj, obj):
    update=False
    add_comma=False
    query='UPDATE currency SET '
    if old_obj.name != obj.name:
      query+='name="{}"'.format(obj.name)
      update=True
      and_comma:True
    if old_obj.symbol != obj.symbol:
      if add_comma:
        query+=", "
      query+='symbol="{}"'.format(obj.symbol)
      update=True
    if update:
      query+=" WHERE ID='{}'".format(obj.code)
      self.cursor.execute(query)
      self.conection.commit()
  
  def save(self, obj):
    try:
        old_obj=self.get(code=obj.code)
    except CurrencyDoesNotExists:
      self.insert(obj)
    else:
      self.update(old_obj, obj)
  
  def delete(self, obj):
    query="DELETE FROM currency WHERE ID='{}'".format(obj.code)
    self.cursor.execute(query)
    self.conection.commit()
    

class Currency(object):
  "Currency Model"
  objects=CurrencyManager(DB_PATH)

  def __init__(self, code, name, symbol):
    self.code = code
    self.name = name
    self.symbol = symbol
  
  def __repr__(self):
    return u'{}'.format(self.name)