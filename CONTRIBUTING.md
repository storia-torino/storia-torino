# Come contribuire

Grazie! Il progetto vive di fonti verificate: ogni contributo deve permettere a chiunque di risalire all'origine di un'informazione.

## Segnalare qualcosa

Apri una *issue* scegliendo il modello giusto:

- **Nuova fonte**: un archivio, un libro, un articolo, un video utile alla knowledge base.
- **Errore di un agente**: una risposta sbagliata, una fonte mancante, un tono fuori posto. Incolla la domanda e la risposta, **senza dati personali**.
- **Nuovo luogo**: un posto di Torino da aggiungere alla mappa.

## Modificare i dati

1. Lavora su un ramo, mai direttamente su `main`.
2. Luoghi: modifica `luoghi/luoghi.geojson` (coordinate in ordine **longitudine, latitudine**) e, se serve, un file in `luoghi/dossier/`.
3. Fonti: aggiungi una riga in `kb/catalogo/sitografia_fonti.csv` con un ID nuovo (S.. per i siti, R.. per le fonti) e lo stato di verifica.
4. Esegui `python luoghi/build/valida.py`: deve rispondere OK.
5. Apri una *pull request*: la revisione è obbligatoria.

## Regole sulle fonti

- Ogni fatto (data, numero, nome) ha una fonte con link o riferimento bibliografico completo.
- Quando le fonti non concordano, si riportano entrambe (vedi i «numeri contesi» nei dossier).
- Lo stato di verifica è esplicito: `sì`, `parziale`, `da verificare`.
- Niente testi o immagini di terzi senza liberatoria: solo metadati e link.

## Cosa non va mai in questo repository

Dati dei partecipanti, chat, questionari, consensi, liste di randomizzazione, chiavi API. Se per errore ne carichi uno, avvisa subito la coordinatrice: rimuoverlo dalla cronologia richiede un intervento apposito.

## Codice di condotta

Discussioni rispettose, anche e soprattutto sui temi contesi (il 1980, il 2011, l'uso delle aree dismesse): si discutono le fonti, non le persone.
