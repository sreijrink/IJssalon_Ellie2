def mijn_functie_1(a):
    resultaat = a * a
    return resultaat

# a = int(input("Voer een getal in? "))
# b = mijn_functie_1(a)
# print(f"Teruggeefwaarde van {a} * {a} is {b}" )


def mijn_functie_2(a, b):
    resultaat = [a + b, a - b, a * b, a // b]
    return resultaat

# a = int(input("Voer een getal in? "))
# b = int(input("Voer een getal in? "))
# resultaat = mijn_functie_2(a, b)
# print(f"Teruggeefwaarde is: {resultaat}")


def laag_en_hoog(mijn_lijst):
    hoogste_waarde = max(mijn_lijst)
    laagste_waarde = min(mijn_lijst)
    return [hoogste_waarde, laagste_waarde]