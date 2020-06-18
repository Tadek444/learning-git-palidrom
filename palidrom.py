
print ("Program sprawdza czy wskazany wyraz jest palidromem.")
        
def palidrom(wyraz):
    wynik = list()
    for litera in wyraz:
        if litera[::-1] == litera:
            wynik.append(True)
        else:
            wynik.append(False)
    return wynik
wyraz = input("Podaj wyraz do sprawdzenia czy jest to palidrom:")
palidrom = palidrom([wyraz])
print (f"Wynik to:{palidrom}")
