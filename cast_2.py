import requests

nazev = input("Zadejte název subjektu: ")

headers = {
     "accept": "application/json",
     "Content-Type": "application/json",
 }

data = f'{{"obchodniJmeno": "{nazev}"}}'

response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data).json()

try:
    pocet_subjektu = response['pocetCelkem']

    print(f"Nalezeno subjektů: {pocet_subjektu}")

    if pocet_subjektu > 0:
        for subjekt in response['ekonomickeSubjekty']:
            obchodni_jmeno = subjekt['obchodniJmeno']
            ico = subjekt['ico']
            print(f"{obchodni_jmeno}, {ico}")
except KeyError:
    print("Chyba: Nebyly nalezeny žádné subjekty.")
