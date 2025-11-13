# C4D-to-Blender-Course

## App di buone notizie

Questo repository contiene una piccola applicazione da riga di comando che
mostra solo buone notizie prese da un archivio curato localmente.

### Requisiti

* Python 3.10 o superiore.

### Utilizzo

```bash
python good_news_app.py            # Mostra una notizia casuale
python good_news_app.py --list     # Elenca più notizie positive
python good_news_app.py --category ambiente --list --limit 3
python good_news_app.py --search vaccino
```

Opzioni disponibili:

* `--category`: filtra per categoria (ad esempio `ambiente`, `salute`).
* `--search`: cerca una parola nel titolo o nel riassunto.
* `--list`: mostra tutte le notizie filtrate anziché una sola casuale.
* `--limit`: numero massimo di elementi mostrati insieme a `--list`.

I dati sono memorizzati in `data/good_news.json` e possono essere estesi con
nuove storie positive.