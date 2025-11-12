# 🔐 TX-Ethereum-Key - Progetto Blockchain Ethereum

Progetto didattico per imparare a interagire con la blockchain Ethereum usando Python e Web3.py.

## 📚 Cosa imparerai

- ✅ Generare un wallet Ethereum
- ✅ Connettersi alla rete Sepolia (testnet)
- ✅ Inviare transazioni con dati personalizzati
- ✅ Leggere e decodificare dati dalla blockchain
- ✅ Gestire variabili d'ambiente in modo sicuro

## 🚀 Quick Start

```bash
# 1. Clona il repository
git clone <url-repository>
cd TX-Ethereum-Key

# 2. Crea ambiente virtuale
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# source venv/bin/activate    # Linux/Mac

# 3. Installa dipendenze
pip install -r requirements.txt

# 4. Configura .env
cp .env.example .env
# Modifica .env con i tuoi dati

# 5. Esegui gli script
python wallet.py      # Genera wallet
python invia_tx.py    # Invia transazione
python leggi_tx.py    # Leggi transazione
```

## 📁 File del Progetto

- `wallet.py` - Genera un nuovo wallet Ethereum
- `invia_tx.py` - Invia una transazione sulla blockchain
- `leggi_tx.py` - Legge dati da una transazione
- `requirements.txt` - Dipendenze Python
- `.env.example` - Template configurazione
- `documentazione.md` - Documentazione completa

## 🔐 Sicurezza

⚠️ **IMPORTANTE**: Il file `.env` contiene informazioni sensibili e NON deve essere committato su GitHub!

- ✅ Il `.gitignore` è già configurato
- ✅ Usa `.env.example` come template
- ✅ Non condividere mai la chiave privata

## 📖 Documentazione Completa

Leggi la [documentazione completa](documentazione.md) per la guida passo-passo dettagliata.

## 🌐 Risorse

- **Faucet Sepolia**: https://cloud.google.com/application/web3/faucet/ethereum/sepolia
- **Etherscan Sepolia**: https://sepolia.etherscan.io/
- **Alchemy**: https://www.alchemy.com/
- **Web3.py Docs**: https://web3py.readthedocs.io/

## 👨‍💻 Autore

Andrea Giovene - ITS ICT Piemonte

---

**Buon coding! 🚀**

