#  Documentazione Progetto Ethereum - Transazioni su Sepolia

##  Obiettivo del Progetto

Questo progetto dimostra come interagire con la blockchain Ethereum utilizzando Python e la libreria Web3.py. Include tre script principali:
1. **wallet.py** - Genera un nuovo wallet Ethereum
2. **invia_tx.py** - Invia una transazione con dati personalizzati sulla rete Sepolia
3. **leggi_tx.py** - Legge e decodifica i dati di una transazione dalla blockchain

---

##  Prerequisiti

- Python 3.8 o superiore
- Account su [Alchemy](https://www.alchemy.com/) o [Infura](https://infura.io/) per ottenere un API key
- SepoliaETH (ETH di test) per pagare le gas fees

---

##  Installazione

### 1. Clona il repository
```bash
git clone <url-del-tuo-repository>
cd TX-Ethereum-Key
```

### 2. Crea un ambiente virtuale (consigliato)
```bash
# Su Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Su Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 4. Configura le variabili d'ambiente
Crea un file `.env` nella root del progetto copiando `.env.example`:
```bash
cp .env.example .env
```

Modifica il file `.env` con i tuoi dati:
```env
SEPOLIA_ENDPOINT_URL=https://eth-sepolia.g.alchemy.com/v2/TUA_API_KEY
MY_PRIVATE_KEY=la_tua_chiave_privata
MY_ADDRESS=0xTuoIndirizzo
TX_HASH_DA_LEGGERE=0xHashTransazione
COGNOME=TuoCognome
```

 **IMPORTANTE**: Non condividere mai il file `.env` o committarlo su GitHub! È già incluso nel `.gitignore`.

---

##  Guida Passo-Passo

### PASSO 1: Genera un Wallet

Esegui lo script `wallet.py` per creare un nuovo wallet Ethereum:

```bash
python wallet.py
```

**Output:**
```
Account creato con successo!
Indirizzo (Address): 0x...
CHIAVE PRIVATA (Private Key): 0x...
```

 **ATTENZIONE**:
- Salva la chiave privata in un posto sicuro
- NON condividerla MAI con nessuno
- Annotati l'indirizzo pubblico

**Cosa fa questo script:**
- Genera una coppia di chiavi crittografiche (privata/pubblica)
- Deriva l'indirizzo Ethereum dalla chiave pubblica
- Non richiede connessione a Internet

---

### PASSO 2: Ottieni l'API Key da Alchemy

1. Vai su [Alchemy](https://www.alchemy.com/)
2. Crea un account gratuito
3. Crea una nuova App:
   - **Chain**: Ethereum
   - **Network**: Sepolia
4. Copia l'**HTTPS endpoint URL**
5. Incolla l'URL nel file `.env` come valore di `SEPOLIA_ENDPOINT_URL`

**Esempio URL:**
```
https://eth-sepolia.g.alchemy.com/v2/abcdefghijklmnopqrstuvwxyz123456
```

---

### PASSO 3: Ottieni SepoliaETH dal Faucet

Sepolia è una rete di test, quindi gli ETH sono gratuiti:

**Opzioni per ottenere SepoliaETH:**

1. **Google Cloud Faucet** (Raccomandato):
   - Vai su [Google Cloud Faucet](https://cloud.google.com/application/web3/faucet/ethereum/sepolia)
   - Accedi con il tuo account Google
   - Inserisci il tuo indirizzo
   - Ricevi 0.05 SepoliaETH

2. **Alchemy Faucet**:
   - Vai su [Alchemy Sepolia Faucet](https://sepoliafaucet.com/)
   - Inserisci il tuo indirizzo
   - Completa il captcha

3. **Altri Faucet**:
   - [Infura Faucet](https://www.infura.io/faucet/sepolia)
   - [QuickNode Faucet](https://faucet.quicknode.com/ethereum/sepolia)

**Verifica il saldo:**
Vai su [Sepolia Etherscan](https://sepolia.etherscan.io/) e cerca il tuo indirizzo per verificare che i fondi siano arrivati.

---

### PASSO 4: Configura il file .env

Inserisci tutti i dati raccolti nel file `.env`:

```env
# URL dell'endpoint Alchemy
SEPOLIA_ENDPOINT_URL=https://eth-sepolia.g.alchemy.com/v2/TUA_API_KEY

# Chiave privata del wallet (generata con wallet.py)
MY_PRIVATE_KEY=0x...

# Indirizzo pubblico del wallet
MY_ADDRESS=0x...

# Il tuo cognome o testo da inserire
COGNOME=Giovene

# Hash della transazione (compilerai questo dopo il Passo 5)
TX_HASH_DA_LEGGERE=
```

---

### PASSO 5: Invia una Transazione

Esegui lo script `invia_tx.py` per inviare una transazione con il tuo cognome sulla blockchain:

```bash
python invia_tx.py
```

**Output atteso:**
```
Connesso a Sepolia. Numero blocco attuale: 9613467
Sto preparando la transazione con data: Giovene (0x47696f76656e65)
Transazione firmata. Invio in corso...
Transazione inviata! Hash (ID): 0xabcdef123456...
In attesa della conferma (mining)...

--- CONFERMATA! ---
Inclusa nel blocco numero: 9613468
Gas utilizzato: 21064
Puoi vederla sull'explorer: https://sepolia.etherscan.io/tx/0xabcdef123456...
```

**Cosa fa questo script:**
1. Si connette alla rete Sepolia tramite Alchemy
2. Converte il tuo cognome in formato esadecimale
3. Crea una transazione verso il tuo stesso indirizzo con valore 0 ETH
4. Include il cognome nel campo `data` della transazione
5. Firma la transazione con la tua chiave privata
6. Invia la transazione alla rete
7. Aspetta la conferma (mining)
8. Mostra i dettagli della transazione

**Costi:**
- Gas utilizzato: ~21,000-25,000 gas
- Costo stimato: ~0.0001 SepoliaETH

---

### PASSO 6: Leggi la Transazione

Copia l'hash della transazione dall'output del Passo 5 e inseriscilo nel file `.env`:

```env
TX_HASH_DA_LEGGERE=0xabcdef123456...
```

Esegui lo script `leggi_tx.py`:

```bash
python leggi_tx.py
```

**Output atteso:**
```
✅ Connesso. Recupero transazione...

--- TRANSAZIONE TROVATA ---
Da: 0xD07e379ea2f8404d3a872577B1a3CF979EDcCD98
A: 0xD07e379ea2f8404d3a872577B1a3CF979EDcCD98
Valore: 0 ETH
Dati (Hex): 0x47696f76656e65
Dati (Testo): 'Giovene'
```

**Cosa fa questo script:**
1. Si connette a Sepolia
2. Recupera la transazione usando l'hash
3. Estrae il campo `input` (dati della transazione)
4. Converte i dati da esadecimale a testo UTF-8
5. Mostra tutti i dettagli della transazione

---

## 🔍 Verifica su Etherscan

Puoi visualizzare la tua transazione su [Sepolia Etherscan](https://sepolia.etherscan.io/):

1. Vai su https://sepolia.etherscan.io/
2. Incolla l'hash della transazione nella barra di ricerca
3. Visualizza:
   - **From**: Il tuo indirizzo
   - **To**: Il tuo indirizzo (transazione a te stesso)
   - **Value**: 0 ETH
   - **Input Data**: Il tuo cognome in formato esadecimale

---

## 📁 Struttura del Progetto

```
TX-Ethereum-Key/
├── wallet.py              # Genera un nuovo wallet Ethereum
├── invia_tx.py           # Invia transazione con dati sulla blockchain
├── leggi_tx.py           # Legge e decodifica dati da una transazione
├── requirements.txt      # Dipendenze Python
├── .env.example         # Template per configurazione
├── .env                 # File di configurazione (NON committare!)
├── .gitignore          # File da escludere da Git
├── documentazione.md   # Questa documentazione
└── readme.md           # Readme del progetto
```

---

## 🔐 Sicurezza

### ⚠️ REGOLE FONDAMENTALI:

1. **MAI committare file sensibili su GitHub:**
   - `.env` contiene chiavi private
   - Usa sempre `.gitignore`

2. **Proteggi la chiave privata:**
   - Non condividerla mai
   - Non inviarla via email/chat
   - Non salvarla su cloud pubblici
   - Chi ha la chiave controlla i fondi

3. **Sepolia vs Mainnet:**
   - Sepolia usa ETH finti (testnet)
   - Mainnet usa ETH reali (costa soldi veri!)
   - Testa SEMPRE su Sepolia prima di usare Mainnet

4. **Variabili d'ambiente:**
   - Usa sempre file `.env` per dati sensibili
   - Non hardcodare mai chiavi nel codice
   - Usa `.env.example` come template pubblico

---

## 🛠️ Risoluzione Problemi

### Errore: "Impossibile connettersi"
- Verifica che l'API key di Alchemy sia corretta
- Controlla la connessione Internet
- Assicurati che l'URL endpoint sia completo

### Errore: "Insufficient funds"
- Il wallet non ha abbastanza SepoliaETH
- Richiedi fondi da un faucet
- Attendi qualche minuto per la conferma

### Errore: "Import dotenv could not be resolved"
- Installa le dipendenze: `pip install -r requirements.txt`
- Verifica che l'ambiente virtuale sia attivo

### Errore: "Nonce too low"
- Una transazione precedente è ancora in sospeso
- Attendi che venga confermata
- Riavvia lo script

### La transazione è "pending" da molto tempo
- La rete potrebbe essere congestionata
- Controlla su Etherscan lo stato
- Potrebbe essere necessario aumentare il gas price

---

## 📚 Concetti Chiave

### Blockchain
Registro distribuito e immutabile dove vengono registrate tutte le transazioni.

### Wallet
- **Chiave Privata**: Password segreta che controlla i fondi
- **Chiave Pubblica**: Derivata dalla privata, usata per verifiche
- **Indirizzo**: Versione corta della chiave pubblica (0x...)

### Transazione
Operazione che trasferisce valore o dati sulla blockchain:
- **From**: Chi invia
- **To**: Chi riceve
- **Value**: Quantità di ETH trasferita
- **Data**: Dati aggiuntivi (es. cognome in esadecimale)
- **Gas**: "Carburante" per eseguire la transazione
- **Nonce**: Contatore progressivo delle transazioni

### Gas
- Unità che misura il costo computazionale
- Gas Price: Quanto paghi per unità di gas (in Gwei)
- Gas Limit: Massimo gas che sei disposto a spendere
- Gas Used: Quanto gas è stato effettivamente usato

### Sepolia
Rete di test di Ethereum dove gli ETH non hanno valore reale.

### Web3.py
Libreria Python per interagire con la blockchain Ethereum.

---

## 🔗 Risorse Utili

- [Web3.py Documentation](https://web3py.readthedocs.io/)
- [Ethereum Documentation](https://ethereum.org/developers)
- [Sepolia Etherscan](https://sepolia.etherscan.io/)
- [Alchemy Tutorials](https://docs.alchemy.com/)
- [Solidity by Example](https://solidity-by-example.org/)

---

## 📝 Note Tecniche

### Codifica Esadecimale
Il testo viene convertito in bytes e poi in formato esadecimale:
```python
"Giovene" → bytes → 0x47696f76656e65
```

### Firma Digitale
La transazione viene firmata con la chiave privata usando ECDSA:
- Garantisce autenticità
- Impedisce modifiche
- Non rivela la chiave privata

### Conferma Blockchain
- La transazione viene inclusa in un blocco
- Il blocco viene aggiunto alla blockchain
- Tempo medio su Sepolia: 12-15 secondi

---

## 🎓 Esercizi Aggiuntivi

1. **Modifica il codice** per inviare anche il nome oltre al cognome
2. **Calcola il costo** totale in USD della transazione
3. **Crea uno script** che legge tutte le transazioni del tuo wallet
4. **Implementa** la gestione di errori più robusta
5. **Aggiungi logging** per tracciare tutte le operazioni

---

## 📄 Licenza

Progetto didattico - ITS ICT Piemonte

---

## 👨‍💻 Autore

Andrea Giovene - ITS ICT Piemonte

---

## 🤝 Contributi

Per contribuire al progetto:
1. Fai un fork del repository
2. Crea un branch per la tua feature
3. Committa le modifiche
4. Apri una Pull Request

---

## ❓ FAQ

**Q: Posso usare questo codice su Mainnet?**  
A: Sì, ma ATTENZIONE! Su Mainnet userai ETH reali. Assicurati di sapere cosa stai facendo.

**Q: Quanto costa una transazione su Mainnet?**  
A: Dipende dal traffico della rete. Può variare da $1 a $50+ in periodi di alta congestione.

**Q: Posso recuperare i fondi se sbaglio indirizzo?**  
A: No, le transazioni blockchain sono irreversibili. Controlla sempre due volte!

**Q: Il file .env è sicuro?**  
A: È sicuro se NON lo condividi e NON lo committi su GitHub. Usa .gitignore!

**Q: Posso usare lo stesso wallet per Mainnet e Testnet?**  
A: Sì, ma è consigliato usare wallet diversi per maggiore sicurezza.

---

**Buon coding! 🚀**
