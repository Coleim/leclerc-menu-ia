#!/usr/bin/env python3
import json
from bs4 import BeautifulSoup

with open("legumes.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

products = []

for item in soup.find_all("li", class_=lambda c: c and "liWCRS310_Product" in c):
    # Name
    name_tag = item.find("a", class_="aWCRS310_Product")
    if not name_tag:
        continue
    # The name is the first text node, weight may follow in a <br> sibling
    name_parts = [t.strip() for t in name_tag.stripped_strings]
    name = " ".join(name_parts) if name_parts else None

    # Origin (optional)
    origin_tag = item.find("span", class_="spanWCRS310_Origine")
    origin = origin_tag.get_text(strip=True) if origin_tag else None

    # Price (integer + decimal parts)
    int_tag = item.find("p", class_="pWCRS310_PrixUnitairePartieEntiere")
    dec_tag = item.find("p", class_="pWCRS310_PrixUnitairePartieDecimale")
    if int_tag and dec_tag:
        price_str = int_tag.get_text(strip=True) + dec_tag.get_text(strip=True).replace(",", ".")
        try:
            price = float(price_str)
        except ValueError:
            price = price_str
    else:
        price = None

    # Price per unit (e.g. €/kg)
    unit_tag = item.find("p", class_="pWCRS310_PrixUniteMesure")
    price_per_unit = unit_tag.get_text(strip=True) if unit_tag else None

    products.append({
        "name": name,
        "origin": origin,
        "price_eur": price,
        "price_per_unit": price_per_unit,
    })

output = json.dumps(products, ensure_ascii=False, indent=2)
print(output)

with open("legumes.json", "w", encoding="utf-8") as f:
    f.write(output)

print(f"\n{len(products)} products written to legumes.json", flush=True)
