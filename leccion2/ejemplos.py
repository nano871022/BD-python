from leccion2.controlador.currency_manager import *
print(10*"#","Currency Manager",10*"#")

peso_argentino=Currency(code="ARS", name="Peso (Argentino)", symbol="$")
dolar = Currency(code="USD", name="Dolar", symbol="U$S")
euro=Currency(code="EUR",name="Euro",symbol="E")

Currency.objects.insert(peso_argentino)
Currency.objects.insert(dolar)
Currency.objects.insert(euro)
try:
  print(Currency.objects.get(code="ARS"))
  print(Currency.objects.filter(code="EUR"))
  print(Currency.objects.filter(name="Dolar"))
  print(Currency.objects.filter(symbol="E"))
  print(Currency.objects.filter())
  print(Currency.objects.get(code="ART"))
except CurrencyDoesNotExists as error:
  print(error)

persos_arg=Currency.objects.get(code="ARS")
Currency.objects.save(persos_arg)

persos_arg=Currency.objects.get(code="ARS")
print(persos_arg.code)
print(persos_arg.name)
print(persos_arg.symbol)

persos_arg.name="Pesos (ARG)"
Currency.objects.save(persos_arg)

persos_arg=Currency.objects.get(code="ARS")
print(persos_arg.code)
print(persos_arg.name)
print(persos_arg.symbol)

pesos_uru = Currency(code="UYU", name="Pesos Uruguayo", symbol="$")

Currency.objects.save(pesos_uru)

persos_arg=Currency.objects.get(code="UYU")
print(persos_arg.code)
print(persos_arg.name)
print(persos_arg.symbol)

pesos_uru=Currency.objects.get("UYU")
Currency.objects.delete(pesos_uru)
try:
  Currency.objects.get("UYU")
except CurrencyDoesNotExists as error:
  print("no encontraod")


print(30*"#")
