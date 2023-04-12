import math

#függvények
def szogfok(sz, m1, m2):
    return math.degrees( math.acos((m1**2 + m2**2 - sz**2)/(2*m1*m2)) )


#1
finp = open("haromszog.txt", mode="rt", encoding="utf-8")
tartalom = finp.read()
finp.close()
adatsorok = tartalom.split('\n')

#2
eredmenyeksorok = []
for sor in adatsorok:
    if sor != '':
        reszletek = sor.split(';')

        a = float(reszletek[0].replace(',' , '.'))
        b = float(reszletek[1].replace(',' , '.'))
        c = float(reszletek[2].replace(',' , '.'))

        alfa = szogfok(a, b, c)
        betta =                            szogfok(b, a, c)
        gamma =szogfok(c, a, b)

        eredmeny = f"{alfa:.2f};{betta:.2f};{gamma:.2f}\n"
        eredmenyeksorok.append(eredmeny)

#3
fout = open("szogek.txt", mode="wt", encoding="utf-8") 
fout.writelines(eredmenyeksorok)
fout.close()       