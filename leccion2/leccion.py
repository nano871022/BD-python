from leccion2.modelo.currency import *
print(10*"#","Currency Manager",10*"#")

peso_argentino=Currency(code="ARS", name="Peso (Argentino)", symbol="$")
dolar = Currency(code="USD", name="Dolar", symbol="U$S")
euro=Currency(code="EUR",name="Euro",symbol="E")

Currency.objects.insert(peso_argentino)
Currency.objects.insert(dolar)
Currency.objects.insert(euro)
print(30*"#")