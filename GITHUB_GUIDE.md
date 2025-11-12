#  Guida per Pubblicare su GitHub

## Prima di Pushare su GitHub

###  Checklist di Sicurezza

Prima di fare il push, verifica che:

- [ ] Il file `.env` sia nella `.gitignore` 
- [ ] Nessuna chiave privata sia presente nel codice
- [ ] Nessun API key sia hardcodato
- [ ] Il file `.env.example` sia presente (senza dati sensibili)
- [ ] Il file `requirements.txt` sia aggiornato

###  Verifica cosa verrà committato

```bash
# Controlla i file che verranno committati
git status

# Assicurati che .env NON sia nella lista!
# Se appare, rimuovilo dalla staging area:
git reset HEAD .env
```

### Se hai già committato dati sensibili

Se hai già committato per errore il file `.env` o altri dati sensibili:

```bash
# Rimuovi il file dalla cronologia Git (ATTENZIONE: riscrive la storia!)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Forza il push (solo se necessario e sai cosa stai facendo)
git push origin --force --all
```

**MEGLIO**: Crea un nuovo repository e ricomincia da capo se hai esposto chiavi sensibili!

##  Preparazione del Repository

### 1. Inizializza Git (se non l'hai già fatto)

```bash
git init
```

### 2. Aggiungi i file

```bash
# Aggiungi tutti i file (eccetto quelli in .gitignore)
git add .

# Verifica cosa stai per committare
git status
```

### 3. Primo Commit

```bash
git commit -m "Initial commit: Progetto Ethereum Sepolia con Python"
```

### 4. Crea il Repository su GitHub

1. Vai su https://github.com
2. Clicca su "New repository"
3. Nome: `TX-Ethereum-Key`
4. Descrizione: `Progetto didattico per interagire con Ethereum usando Python e Web3.py`
5. **NON** inizializzare con README (lo hai già)
6. Clicca "Create repository"

### 5. Collega e Pusha

```bash
# Aggiungi il remote
git remote add origin https://github.com/TUO_USERNAME/TX-Ethereum-Key.git

# Rinomina il branch principale (opzionale)
git branch -M main

# Pusha il codice
git push -u origin main
```

## Comandi Git Utili

```bash
# Stato del repository
git status

# Vedi le differenze
git diff

# Aggiungi file specifici
git add file.py

# Commit con messaggio
git commit -m "Descrizione delle modifiche"

# Pusha le modifiche
git push

# Aggiorna dal repository remoto
git pull

# Vedi la cronologia
git log --oneline

# Crea un nuovo branch
git checkout -b nome-feature

# Torna al branch main
git checkout main
```

## Protezione Extra

### Aggiungi Pre-commit Hook (Opzionale)

Crea il file `.git/hooks/pre-commit`:

```bash
#!/bin/bash

# Verifica che .env non sia nella staging area
if git diff --cached --name-only | grep -q "^.env$"; then
    echo "ERRORE: Stai cercando di committare il file .env!"
    echo "Rimuovilo con: git reset HEAD .env"
    exit 1
fi

echo "Controllo sicurezza superato"
exit 0
```

Rendilo eseguibile:
```bash
chmod +x .git/hooks/pre-commit
```

### Usa GitHub Secrets per CI/CD

Se usi GitHub Actions, salva i segreti in:
- Settings → Secrets and variables → Actions
- Aggiungi:
  - `SEPOLIA_ENDPOINT_URL`
  - `MY_PRIVATE_KEY`
  - `MY_ADDRESS`

## Best Practices

1. **Commit frequenti**: Fai commit piccoli e descrittivi
2. **Branch per feature**: Usa branch separati per nuove funzionalità
3. **Pull Request**: Usa PR anche se lavori da solo (buona pratica)
4. **Tag per versioni**: Usa `git tag v1.0.0` per marcare versioni
5. **README aggiornato**: Mantieni sempre aggiornata la documentazione

## Messaggi di Commit Efficaci

Usa il formato:
```
tipo: breve descrizione

Descrizione più dettagliata se necessaria
```

Tipi comuni:
- `feat`: Nuova funzionalità
- `fix`: Correzione bug
- `docs`: Documentazione
- `refactor`: Refactoring codice
- `test`: Aggiunti test
- `chore`: Manutenzione

Esempi:
```bash
git commit -m "feat: aggiungi supporto per multi-firma"
git commit -m "fix: correggi gestione errori in leggi_tx.py"
git commit -m "docs: aggiorna README con istruzioni Docker"
```

## Rendi il Repo Attraente

### Aggiungi Badges al README

```markdown
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Web3.py](https://img.shields.io/badge/web3.py-6.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
```

### Aggiungi Topics su GitHub

Nel repository su GitHub:
- Settings → Topics
- Aggiungi: `ethereum`, `blockchain`, `web3`, `python`, `sepolia`, `testnet`

### Crea una GitHub Page (Opzionale)

Per pubblicare la documentazione come sito web.

---

**Buon push! **

**Ricorda**: Una volta che qualcosa è su GitHub, consideralo pubblico per sempre!
