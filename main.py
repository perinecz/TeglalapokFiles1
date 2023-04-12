#függvények
def kerulet(aa, bb):
    return 2*(aa + bb)

def terulet(aa, bb):
    return aa * bb

def atlo(aa, bb):
    return (aa**2 + bb**2) ** (1/2)

#1
finp = open("teglalapok.txt", mode="rt", encoding="utf-8")
tartalom = finp.read()
finp.close()
adatSorok = tartalom.split('\n')

#2
eredmenySorok = []
for item in adatSorok:
    if item != '':
        reszletek = item.split(';')

        a = float(reszletek[0].replace(',' , '.'))
        b = float(reszletek[1].replace(',' , '.'))

        d = atlo(a, b)
        K = kerulet(a, b)
        T = terulet(a, b)

        eredmeny = f"{d:.2f};{K:.2f};{T:.2f}"
        eredmenySorok.append(eredmeny)

#
tartalom = '\n'.join(eredmenySorok)
fout = open("kerulet-terulet.txt", mode="wt", encoding="utf-8")
fout.write(tartalom)
fout.close()