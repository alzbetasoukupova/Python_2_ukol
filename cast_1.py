import requests

ico = input("Zadejte IČO subjektu: ")
url = (f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
response = requests.get(url).json()

obchodni_jmeno = response["obchodniJmeno"]
adresa = response["sidlo"]["textovaAdresa"]

print(obchodni_jmeno, adresa)
