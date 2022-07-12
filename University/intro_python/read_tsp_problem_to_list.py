
def readProblem(dosyaAdi):
  dosyaProblem = open(dosyaAdi,'r')
  icerik = dosyaProblem.read()
  aa = icerik.split("\n")
  data = []
  for a in aa[6:-2]:
    bb=a.split(' ')
    satir = []
    for b in bb:
      satir.append(int(b))
    data.append(satir)
  dosyaProblem.close
  return data
dosya1 = 'w13b- 22, 23 Apr/att48-2.tsp'

veriler = readProblem(dosya1)

verilerD = {}
for v in veriler:
  verilerD[v[0]]=v[1:]

def uzaklik(a,b):
  return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**.5 



print(verilerD[4])

print(uzaklik(verilerD[3], verilerD[4]))
