# Luoghi

| File | Contenuto |
|---|---|
| `luoghi.geojson` | I luoghi (L01…), schema in [`docs/schema-dati.md`](../docs/schema-dati.md) |
| `dossier/` | Un file per dossier: materiali ordinati per tipo e per punto di vista |
| `luoghi.kml` | Generato: da importare in Google Earth web |
| `inventario_siti.csv` | 25 siti industriali e riconvertiti (uso, chiusura, nuovo uso, stato 2026, fonti), dal dossier del 27/11/2026: candidati per i prossimi luoghi L13… |
| `build/build.py` | Genera `mappa/index.html` e `luoghi.kml` |
| `build/valida.py` | Controlli automatici sui dati |
| `build/sfondo_osm.geojson` | Confine comunale, fiumi e Valentino da OpenStreetMap (sfondo vettoriale per le anteprime offline) |

Coordinate: OpenStreetMap Nominatim, 2/11/2026 (© OpenStreetMap contributors, ODbL). Per Mirafiori il punto è sul civico di corso Agnelli 200, non al centro dello stabilimento.

## Immagini (27/11/2026)

22 foto con licenza aperta da Wikimedia Commons su 7 luoghi, divise in «prima» e «dopo»: L01 Lingotto 4, L02 Mirafiori 4, L03 OGR 4, L04 Teatro Nuovo 1, L05 Piazza San Carlo 2, L06 Parco Dora 4, L12 Grattacielo Lancia 3. Mancano L07–L11. Le copie di lavoro, con il registro dei crediti, sono nel Drive del progetto (02.D Immagini, `id_drive`). Regole: [`docs/schema-dati.md`](../docs/schema-dati.md#immagini-di-un-luogo).

## Stato della verifica (v0.1.0)

| ID | Luogo | Verifica |
|---|---|---|
| L01–L03, L05, L08, L09 | Lingotto, Mirafiori, OGR, Piazza San Carlo, Polo del '900, Centro Storico Fiat | sì |
| L04 | Teatro Nuovo (dossier marcia dei 40mila, 18 materiali) | sì |
| L06, L07 | Parco Dora, Cittadella Politecnico | parziale |
| L10–L12 | Ex Incet, Docks Dora, Grattacielo Lancia | da verificare |
