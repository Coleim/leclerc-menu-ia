#!/usr/bin/env python3
import json
import glob
import os
from bs4 import BeautifulSoup

html_files = glob.glob("*.html")
all_products = []

for html_file in sorted(html_files):
    category = os.path.splitext(html_file)[0]
    with open(html_file, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    count = 0
    for item in soup.find_all("li", class_=lambda c: c and "liWCRS310_Product" in c):
        # Name
        name_tag = item.find("a", class_="aWCRS310_Product")
        if not name_tag:
            continue
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

        all_products.append({
            "category": category,
            "name": name,
            "origin": origin,
            "price_eur": price,
            "price_per_unit": price_per_unit,
        })
        count += 1

    print(f"  {html_file}: {count} products")

output = json.dumps(all_products, ensure_ascii=False, indent=2)

with open("products.json", "w", encoding="utf-8") as f:
    f.write(output)

print(f"\nTotal: {len(all_products)} products written to products.json")
