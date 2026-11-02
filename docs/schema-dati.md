# Schema dei dati

## Luogo (`luoghi/luoghi.geojson`, una *Feature* per luogo)

Geometria: `Point`, coordinate `[longitudine, latitudine]` in WGS84 (EPSG:4326). I dati del Comune di Torino sono spesso in Monte Mario (EPSG:3003) e vanno convertiti.

| Campo | Tipo | Esempio | Note |
|---|---|---|---|
| `id` | testo | `L04` | Stabile: gli agenti lo citano |
| `nome` | testo | `Teatro Nuovo` | |
| `categoria` | `fabbrica` \| `riconvertita` \| `evento` \| `archivio` | `evento` | Colore sulla mappa |
| `agenti` | lista di `R`, `G`, `F` | `["G"]` | Chi ne parla |
| `anno_chiave` | intero o null | `1980` | |
| `testo_breve` | testo, max 60 parole | | Scritto per 18-35enni |
| `fonti` | lista di `{id, titolo, url}` | | ID del catalogo (A01…, S01…, R01…) |
| `immagini` | lista di `{url, didascalia, autore, anno, licenza, id_liberatoria}` | `[]` | Solo con liberatoria (strato G) |
| `verificato` | testo | `sì`, `parziale`, `da verificare` | |
| `coord_fonte` | testo | `OpenStreetMap Nominatim, 2/11/2026` | |
| `dossier` | percorso o assente | `dossier/L04-marcia-40mila.json` | |

## Dossier (`luoghi/dossier/<ID>-<slug>.json`)

| Campo | Contenuto |
|---|---|
| `luogo` | ID del luogo |
| `titolo`, `sintesi` | Titolo dell'evento o del tema; sintesi di 2-3 frasi |
| `numeri_contesi` | Facoltativo: cifre che cambiano secondo la fonte, con le fonti |
| `materiali` | Lista di materiali (sotto) |

Materiale:

| Campo | Valori |
|---|---|
| `tipo` | `Fonte primaria`, `Testimonianza`, `Ricostruzione`, `Studio`, `Immagini`, `Video` |
| `prospettiva` | `aziendale/quadri`, `sindacale/operaia`, `giornalistica`, `storiografica`, `politica` |
| `titolo`, `fonte`, `anno`, `url`, `nota` | Descrizione; `url` vuoto se non disponibile |
| `accesso` | `open`, `gratuito`, `a pagamento`, `da reperire`… |
| `verifica` | Stato della verifica |

La `prospettiva` permette di filtrare i materiali per punto di vista: è la regola 5 delle linee guida degli agenti («mostra più punti di vista sui temi contesi») tradotta in dati.

## Documento della knowledge base (metadati)

Dieci campi, dalla struttura KB v1:

| Campo | Valori |
|---|---|
| `tipo_fonte` | saggio, report, testimonianza, articolo, video, scheda luogo, statistica, timeline |
| `scala` | città, quartiere, luogo, persona, tema |
| `periodo` | boom, crisi, anni 80-90, oggi, transizione lunga |
| `tema` | lavoro, casa, scuola, migrazione, giovani, identità, impresa, spazio pubblico, cultura, futuro |
| `registro` | storico, sociologico, narrativo, giornalistico, statistico |
| `uso_previsto` | risposta fattuale, racconto immersivo, confronto passato-presente, attivazione discussione |
| `sensibilita` | bassa, media, alta |
| `luogo` | Mirafiori Sud, Mirafiori Nord, Torino, Ivrea, Parco Dora… (o ID L..) |
| `attendibilita` | primaria, secondaria, giornalistica, divulgativa |
| `agenti` | Riccardo, Giovanni, Fatima, Guida |

Lo schema formale è in [`kb/schema/metadati.schema.json`](../kb/schema/metadati.schema.json).
