from leccion2.controlador.currency_manager import *
from leccion2.constantes.constante import *


class Currency(object):
  "Currency Model"
  objects=CurrencyManager(DB_PATH)

  def __init__(self, code, name, symbol):
    self.code = code
    self.name = name
    self.symbol = symbol
  
  def __repr__(self):
    return u'{}'.format(self.name)