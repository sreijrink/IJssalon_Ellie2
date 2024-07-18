from algemene_functies import mijn_functie_2

# Les 8 opdracht 5
def aanbieding_1(smaak, prijs, korting):
    prijs_korting = prijs * korting
    prijs_aanbieding = prijs - prijs_korting
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_aanbieding:.2f} euro."

print(aanbieding_1("aardbei", 4, float(0.1)))


print()
# Les 8 opdracht 6
# Les 8 opdracht 7 - btw
def inkomsten_totaal(inkomsten, btw):
        return [sum(inkomsten), sum(inkomsten) *btw]

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
totaal = inkomsten_totaal(inkomsten_per_dag, 0.09)
bedrag = totaal[0]

print(f"Totaal inkomsten: €{totaal[0]:.2f}")
print(f"Het totaal van alle inkomsten van deze week is {totaal[0]:.2f} euro, waarover {totaal[1]:.2f} euro btw betaald dient te worden.")


print()
# Les 8 opdracht 8
def laag_en_hoog(mijn_lijst):
    hoogste_waarde = max(mijn_lijst)
    laagste_waarde = min(mijn_lijst)
    return [hoogste_waarde, laagste_waarde]

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten_per_dag)
print(f"Hoogste waarde: {resultaat[0]}, Laagste waarde: {resultaat[1]}")


print()
# Les 8 opdracht 9 + 10
def gemiddelde(mijn_lijst):
    average = sum(mijn_lijst) / len(mijn_lijst)
    return average
    
resultaat = gemiddelde([220, 430, 125, 160, 205, 90, 345])
print(f"De gemiddelde inkomsten deze week zijn {resultaat:.2f} euro.")


print()
# Les 8 opdracht 11
def meervoudig(invoer_lijst):
    hoogste_waarde = max(invoer_lijst)
    laagste_waarde = min(invoer_lijst)
    return [hoogste_waarde, laagste_waarde]

resultaat = meervoudig([10, 5, 3, 2, 1, 2, 9])
print(resultaat)


print()
# les 8 opdracht 12
from algemene_functies import mijn_functie_2
from algemene_functies import laag_en_hoog

def combinatie(invoer_lijst2):
    korte_lijst = laag_en_hoog(invoer_lijst2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

c = combinatie([10, 5, 3, 2, 1, 2, 9])
print(c)