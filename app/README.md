# Applicazione

Spazio del developer: recupero dalle fonti (RAG), prompt degli agenti, interfaccia di chat, registrazione delle sessioni.

## Requisiti principali

I requisiti completi sono nel documento «Requisiti tecnici developer v1» (Drive, cartella 04.1). In sintesi:

- legge i prompt da `agenti/` e i metadati da `kb/` (schema in `kb/schema/metadati.schema.json`);
- mostra una scheda fonte per ogni fatto (regola 2) e può rimandare ai luoghi della mappa per ID (`L04`…);
- registra le sessioni con l'ID pseudonimo assegnato (S1-01…), **senza nomi né email**;
- salva i log **solo** nello spazio riservato UniTo, mai nel repository;
- espone la versione degli agenti in ogni risposta registrata (per verificare il congelamento).

## Segreti

Chiavi API e credenziali vanno nei *secrets* di GitHub o in un file `.env` locale (escluso da git). Usa `.env.example` come modello.

## Indice della knowledge base

L'indice vettoriale viene costruito dai testi della cartella riservata (anche testi di terzi con liberatoria) e **non** va nel repository (`app/indice/` e `app/vectorstore/` sono in `.gitignore`).
