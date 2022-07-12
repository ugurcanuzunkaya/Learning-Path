plakaDosyaAdi = 'w13b- 22, 23 Apr/plakalar1.csv'

dosya = open(plakaDosyaAdi, 'r')
tumVeriler = dosya.read()
plakalar = tumVeriler.split('\n')


plakaD = {'key': 'value'}
for sehir in plakalar:
  kod, sehirAdi = sehir.split(';')
  plakaD[sehirAdi]=kod
  plakaD[kod]=sehirAdi
 
print(plakaD['Ardahan'])
print(plakaD['Adana'])

print(plakaD['34'])
print(plakaD['26'])

print(plakaD.keys()[81])