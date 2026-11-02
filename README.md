# Stor-IA di Torino

Tre agenti conversazionali, **Riccardo**, **Giovanni** e **Fatima**, raccontano a ragazze e ragazzi tra i 18 e i 35 anni la deindustrializzazione di Torino: la fabbrica, la sua crisi, le trasformazioni della città. Ogni risposta mostra le fonti da cui viene. Il progetto misura con un esperimento randomizzato se questo modo di raccontare la storia aumenta conoscenza e coinvolgimento rispetto ai materiali curati dagli enti.

> Progetto sostenuto da Fondazione CRT (Bando 2025) e Banca d'Italia, su Torino industriale e post-industriale. Partner: [*da completare*].
> Stato: **in sviluppo**, sperimentazione tra il 24 novembre e il 3 dicembre 2026.

## Cosa trovi qui

| Cartella | Contenuto | Licenza |
|---|---|---|
| [`kb/`](kb/) | Knowledge base: catalogo delle fonti, sitografia, schema dei metadati, testi aperti | Metadati CC0, testi CC BY 4.0 |
| [`luoghi/`](luoghi/) | I luoghi della deindustrializzazione (GeoJSON), dossier per luogo, script di build | ODbL 1.0 |
| [`mappa/`](mappa/) | La mappa interattiva, pubblicata con GitHub Pages | MIT (codice) |
| [`agenti/`](agenti/) | Personaggi, regole comuni, prompt versionati, set di valutazione | CC BY 4.0 |
| [`app/`](app/) | Applicazione conversazionale (recupero dalle fonti, interfaccia) | MIT |
| [`strumenti/`](strumenti/) | Strumenti di misura dell'esperimento (riferimenti e scoring) | CC BY 4.0 |
| [`analisi/`](analisi/) | Analisi di potenza, randomizzazione, piano di analisi, script | MIT |
| [`docs/`](docs/) | Protocollo pubblico, schema dei dati, registro delle decisioni | CC BY 4.0 |

Dettagli in [`LICENSE`](LICENSE) e [`LICENSE-CONTENUTI.md`](LICENSE-CONTENUTI.md).

## Cosa NON trovi qui (e perché)

- **Dati dei partecipanti**: chat, questionari, consensi. Sono dati personali e restano nello spazio riservato dell'Università di Torino, come previsto dall'informativa. A fine progetto un dataset anonimizzato sarà depositato su Zenodo.
- **Lista di randomizzazione e seme**: sono riservati fino all'ultimo incontro (3/12/2026) per garantire l'occultamento dell'assegnazione; poi saranno pubblicati qui.
- **Testi e immagini di terzi** (articoli, libri, foto d'agenzia): nel catalogo ci sono solo metadati e link. Gli agenti li usano solo se abbiamo il permesso.

## Provare la mappa in locale

```bash
python luoghi/build/valida.py   # controlla i dati
python luoghi/build/build.py    # genera mappa/index.html e luoghi/luoghi.kml
```

Poi apri `mappa/index.html` nel browser. Il file `luoghi/luoghi.kml` si importa in Google Earth web (Progetti → Nuovo → Importa file KML).

## Versioni

Le versioni seguono il calendario dell'esperimento. Ogni release è archiviata su Zenodo con un DOI.

| Versione | Data | Cosa |
|---|---|---|
| v0.1.0 | 2/11/2026 | Struttura del repository, catalogo, primi 12 luoghi |
| v0.9.0 | 19/11/2026 | Versione del pilota |
| **v1.0.0** | **23/11/2026** | **Agenti congelati: la versione usata in tutti e quattro gli incontri** |
| v1.1.0 | 15/12/2026 | Report, seme e lista di randomizzazione, dati anonimizzati |

## Come citare

Vedi [`CITATION.cff`](CITATION.cff); GitHub mostra il pulsante «Cite this repository».

## Contribuire

Segnalazioni di fonti, errori degli agenti o nuovi luoghi: apri una *issue* con i modelli proposti. Vedi [`CONTRIBUTING.md`](CONTRIBUTING.md).
