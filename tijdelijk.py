from helper import decoreer

# 7.15 Huiswerkopgave
def print_aanbieding():
    prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }

    # 7.15.3
    aanbieding = prijzen["aardbei"] * 0.8
    # print (aanbieding)

    # 7.15.4
    reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
    # print (reclame_tekst)


    # 7.15.5
    reclame_tekst2 = reclame_tekst[:-14]
    # print (reclame_tekst2)


    # 7.15.6
    reclame_tekst3 = reclame_tekst2.upper() 
    # print (reclame_tekst3)

    # 7.15.7
    reclame_tekst4 = reclame_tekst3.split()
    # print (reclame_tekst4)


    # 7.15.8
    for el in reclame_tekst4:
    #    print(el)
        
    # 7.15.9
    #    print(el.lower())

    # 7.15.10
        if len(el) > 4:
            print(el.upper())
        else:
            print(el.lower())

decoreer("Aanbieding")
print_aanbieding()