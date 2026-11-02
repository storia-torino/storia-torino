"""Stor-IA di Torino — lista di randomizzazione per i 4 incontri.

- 32 ID per incontro (25 attesi + overbooking per chi non si presenta)
- bracci A (agenti) / B (contenuti curati dagli enti, poi agenti) 1:1,
  in blocchi permutati di 4 dentro ogni incontro
- ordine dei tre agenti ruotato sulle 6 permutazioni, bilanciato dentro ogni braccio

OCCULTAMENTO DELL'ASSEGNAZIONE
Il seme NON è nel repository: chi conosce il seme può ricostruire la lista.
Lo script lo legge dalla variabile d'ambiente STORIA_SEME oppure dal file
`analisi/privato/seme.txt` (escluso da git con .gitignore). La lista generata
va salvata nello spazio riservato UniTo, non qui. Seme e lista verranno
pubblicati dopo l'ultimo incontro (3/12/2026).

Uso:
    STORIA_SEME=<seme> python analisi/randomizza.py --out <percorso_riservato>/lista.csv
"""
import argparse
import csv
import itertools
import os
import random
from pathlib import Path


def leggi_seme():
    if os.environ.get("STORIA_SEME"):
        return int(os.environ["STORIA_SEME"])
    f = Path(__file__).parent / "privato" / "seme.txt"
    if f.exists():
        return int(f.read_text().strip())
    raise SystemExit("Seme mancante: imposta STORIA_SEME o crea analisi/privato/seme.txt (non versionato).")


def genera(seme, sessioni=(1, 2, 3, 4), per_sessione=32):
    rng = random.Random(seme)
    ordini = list(itertools.permutations(["Riccardo", "Giovanni", "Fatima"]))
    righe, k = [], {"A": 0, "B": 0}
    for s in sessioni:
        bracci = []
        while len(bracci) < per_sessione:
            blocco = ["A", "A", "B", "B"]
            rng.shuffle(blocco)
            bracci += blocco
        for i, br in enumerate(bracci, start=1):
            righe.append({"id": f"S{s}-{i:02d}", "sessione": s, "braccio": br,
                          "ordine_agenti": " > ".join(ordini[k[br] % 6])})
            k[br] += 1
    return righe


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="percorso del CSV, FUORI dal repository")
    a = ap.parse_args()
    out = Path(a.out).resolve()
    if Path(__file__).resolve().parents[1] in out.parents and "privato" not in out.parts:
        raise SystemExit("Non scrivere la lista dentro il repository: usa lo spazio riservato UniTo.")
    righe = genera(leggi_seme())
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=righe[0].keys())
        w.writeheader()
        w.writerows(righe)
    print(f"{len(righe)} ID scritti in {out}")
