"""Genera mappa/index.html e luoghi/luoghi.kml da luoghi/luoghi.geojson e luoghi/dossier/*.json.

Uso (dalla radice del repository):
    python luoghi/build/build.py

Nessuna dipendenza esterna: solo libreria standard di Python 3.9+.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LUOGHI = ROOT / "luoghi"
VERSIONE = (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").exists() else "dev"

COL_KML = {"fabbrica": "ff2e3ab2", "riconvertita": "ff6d7d2f", "evento": "ff1d78c7", "archivio": "ff925b3b"}  # aabbggrr
AGENTI = {"R": "Riccardo", "G": "Giovanni", "F": "Fatima"}


def carica():
    """Legge i luoghi e incorpora i dossier referenziati."""
    fc = json.loads((LUOGHI / "luoghi.geojson").read_text(encoding="utf-8"))
    for f in fc["features"]:
        p = f["properties"]
        if isinstance(p.get("dossier"), str):
            p["dossier"] = json.loads((LUOGHI / p["dossier"]).read_text(encoding="utf-8"))
    return fc


def scrivi_mappa(fc):
    t = (LUOGHI / "build" / "template.html").read_text(encoding="utf-8")
    t = t.replace("/*LUOGHI*/", json.dumps(fc, ensure_ascii=False)).replace("/*VERSIONE*/", VERSIONE)
    out = ROOT / "mappa" / "index.html"
    out.write_text(t, encoding="utf-8")
    return out


def scrivi_kml(fc):
    e = html.escape
    k = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<kml xmlns="http://www.opengis.net/kml/2.2"><Document>',
         f"<name>Stor-IA di Torino — luoghi {e(VERSIONE)}</name>",
         "<description>Strato D della KB. Coordinate © OpenStreetMap contributors (ODbL).</description>"]
    for cat, col in COL_KML.items():
        k.append(f'<Style id="{cat}"><IconStyle><color>{col}</color><scale>1.1</scale><Icon>'
                 '<href>http://maps.google.com/mapfiles/kml/paddle/wht-blank.png</href></Icon></IconStyle></Style>')
    for cat in COL_KML:
        k.append(f"<Folder><name>{cat.capitalize()}</name>")
        for f in fc["features"]:
            p = f["properties"]
            if p["categoria"] != cat:
                continue
            lon, lat = f["geometry"]["coordinates"][:2]
            fonti = "<br/>".join(f'<a href="{s["url"]}">{e(s["id"])} · {e(s["titolo"])}</a>' for s in p["fonti"])
            d = (f'<p>{e(p["testo_breve"])}</p><p><i>Ne parla: {", ".join(AGENTI[a] for a in p["agenti"])}</i></p>'
                 f'<p><b>Fonti</b><br/>{fonti}</p><p><small>Verifica: {e(p["verificato"])} · {p["id"]}</small></p>')
            if isinstance(p.get("dossier"), dict):
                D = p["dossier"]
                d += f'<hr/><p><b>Dossier: {e(D["titolo"])}</b></p><p>{e(D["sintesi"])}</p>'
                if D.get("numeri_contesi"):
                    d += f'<p><i>Numeri contesi: {e(D["numeri_contesi"])}</i></p>'
                tipi = list(dict.fromkeys(m["tipo"] for m in D["materiali"]))
                for tp in tipi:
                    voci = [(f'<a href="{m["url"]}">{e(m["titolo"])}</a>' if m["url"] else e(m["titolo"]))
                            + f' — {e(m["fonte"])} [{e(m["prospettiva"])}]'
                            for m in D["materiali"] if m["tipo"] == tp]
                    d += f"<p><b>{e(tp)}</b><br/>" + "<br/>".join(voci) + "</p>"
            k.append(f'<Placemark><name>{e(p["nome"])}</name><styleUrl>#{cat}</styleUrl>'
                     f"<description><![CDATA[{d}]]></description>"
                     f"<Point><coordinates>{lon},{lat},0</coordinates></Point></Placemark>")
        k.append("</Folder>")
    k.append("</Document></kml>")
    out = LUOGHI / "luoghi.kml"
    out.write_text("\n".join(k), encoding="utf-8")
    return out


if __name__ == "__main__":
    fc = carica()
    print("scritto", scrivi_mappa(fc).relative_to(ROOT))
    print("scritto", scrivi_kml(fc).relative_to(ROOT))
