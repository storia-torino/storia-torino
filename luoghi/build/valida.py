"""Controlli automatici sui dati (eseguiti anche da GitHub Actions a ogni modifica).

- ogni luogo ha i campi obbligatori, un ID unico L00 (o L000) e coordinate dentro l'area di Torino
- ogni fonte citata ha un URL o è segnata come da verificare
- ogni dossier referenziato esiste ed è JSON valido
- i CSV del catalogo hanno ID unici
Uso: python luoghi/build/valida.py
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errori = []

OBBLIGATORI = ["id", "nome", "categoria", "agenti", "testo_breve", "fonti", "verificato"]
CATEGORIE = {"fabbrica", "riconvertita", "evento", "archivio"}
BBOX = (7.50, 44.95, 7.85, 45.20)  # lon_min, lat_min, lon_max, lat_max (Torino e cintura)

fc = json.loads((ROOT / "luoghi" / "luoghi.geojson").read_text(encoding="utf-8"))
visti = set()
for f in fc["features"]:
    p = f["properties"]
    pid = p.get("id", "?")
    for c in OBBLIGATORI:
        if c not in p:
            errori.append(f"{pid}: manca il campo '{c}'")
    if not re.fullmatch(r"L\d{2,3}", pid):
        errori.append(f"{pid}: ID non nel formato L00 o L000")
    if pid in visti:
        errori.append(f"{pid}: ID duplicato")
    visti.add(pid)
    if p.get("categoria") not in CATEGORIE:
        errori.append(f"{pid}: categoria '{p.get('categoria')}' non ammessa")
    lon, lat = f["geometry"]["coordinates"][:2]
    if not (BBOX[0] <= lon <= BBOX[2] and BBOX[1] <= lat <= BBOX[3]):
        errori.append(f"{pid}: coordinate fuori da Torino ({lon}, {lat}); ricorda: GeoJSON vuole lon, lat")
    if isinstance(p.get("dossier"), str):
        path = ROOT / "luoghi" / p["dossier"]
        if not path.exists():
            errori.append(f"{pid}: dossier {p['dossier']} non trovato")
        else:
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                errori.append(f"{pid}: dossier non è JSON valido ({e})")

for nome in ["catalogo_fonti.csv", "sitografia_fonti.csv"]:
    righe = list(csv.DictReader((ROOT / "kb" / "catalogo" / nome).open(encoding="utf-8")))
    ids = [r["ID"] for r in righe]
    doppi = {i for i in ids if ids.count(i) > 1}
    if doppi:
        errori.append(f"{nome}: ID duplicati {sorted(doppi)}")

if errori:
    print("\n".join("ERRORE " + e for e in errori))
    sys.exit(1)
print(f"OK: {len(visti)} luoghi, cataloghi senza ID duplicati")
