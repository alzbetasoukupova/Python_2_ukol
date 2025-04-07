# ZADANI

# Část 1

# V této části vyhledej informace o konkrétním subjektu na základě jeho identifikačního čísla (IČO).
# Toto číslo je jedinečným identifikátorem subjektu, pro každé číslo tedy rejstřík vrátí informace pouze o jednom subjektu.

# Nejprve se pomocí funkce input() zeptej uživatele nebo uživatelky, o kterém subjektu chce získat informace.
# S využitím modulu requests odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO, kde ICO nahraď číslem,
# které zadal(ka) uživatel(ka) (např. https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22834958).
# S adresou pracuj jako s obyčejným řetězcem, tj. můžeš využívat formátované řetězce, metodu .replace(), operátor + atd.
# Text, který API vrátí, převeď na JSON a zjisti z něj obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle textovaAdresa).
# Získané informace vypiš na obrazovku.


#RESENI

import requests

ico = input("Zadejte IČO subjektu: ")
url = (f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
response = requests.get(url)

data = response.json()
#print(data) - vypsani veskereho infa

obchodni_jmeno = data["obchodniJmeno"]
adresa = data["sidlo"]["textovaAdresa"]

print(obchodni_jmeno)
print(adresa)

# Například pro IČO 22834958 by tvůj program měl vypsat následující text.

# Czechitas z.ú.
# Krakovská 583/9, Nové Město, 110 00 Praha 1