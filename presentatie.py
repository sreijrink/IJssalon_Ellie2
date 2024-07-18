# def presenteer(mijn_dict, totaal):
def presenteer(dictionary, totaal):
    for sleutel, waarde in dictionary.items():
        print(f"{sleutel} : {waarde} euro")
    print("==========================") # 26x =
    print(f"totaal : {totaal} euro")

# mijn_dict = {"vis" : 10, "vlees" : 25, "overig" : 15}
# totaal = sum(mijn_dict.values())
# presenteer(mijn_dict, totaal)