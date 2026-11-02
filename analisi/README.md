# Analisi

| File | Cosa fa |
|---|---|
| `potenza.py` | Effetto minimo rilevabile: confronto tra bracci (ANCOVA, t non centrale) ed entro soggetto |
| `randomizza.py` | Genera la lista di randomizzazione (blocchi di 4, ordine degli agenti bilanciato). **Il seme non è nel repository** |
| `piano_analisi.md` | Piano di analisi preregistrato (da completare prima del 24/11 e depositare su OSF) |

## Risultati dell'analisi di potenza (α = 0,05, potenza 0,80)

| Confronto | Effetto minimo rilevabile |
|---|---|
| A vs B, 50+50, ANCOVA con r = 0,5 | d = 0,49 |
| A vs B, 50+50, senza covariata | d = 0,57 |
| Entro soggetto tra agenti, n = 100 | dz = 0,28 |
| Quattro bracci da 25 (disegno originale) | d = 0,70 |

## Dati

Gli script di analisi lavoreranno su `dati_sintetici/` (generati per testare il codice) finché la raccolta non è conclusa. I dati reali restano nello spazio riservato UniTo; il dataset anonimizzato sarà depositato su Zenodo con la release v1.1.0.
