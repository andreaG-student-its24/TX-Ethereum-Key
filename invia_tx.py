from web3 import Web3
import os
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# --- 1. CONFIGURAZIONE ---
# Leggi le configurazioni dal file .env
SEPOLIA_ENDPOINT_URL = os.getenv('SEPOLIA_ENDPOINT_URL')
MY_PRIVATE_KEY = os.getenv('MY_PRIVATE_KEY')
MY_ADDRESS = os.getenv('MY_ADDRESS')
COGNOME = os.getenv('COGNOME', 'Giovene')  # Valore di default se non specificato

# Verifica che le variabili siano state caricate
if not all([SEPOLIA_ENDPOINT_URL, MY_PRIVATE_KEY, MY_ADDRESS]):
    print("Errore: Assicurati di aver creato il file .env con tutte le configurazioni necessarie.")
    print("Usa .env.example come template.")
    exit()

# --- 2. CONNESSIONE ---
w3 = Web3(Web3.HTTPProvider(SEPOLIA_ENDPOINT_URL))

if not w3.is_connected():
    print("Errore: Impossibile connettersi all'endpoint Sepolia.")
    exit()

print(f"Connesso a Sepolia. Numero blocco attuale: {w3.eth.block_number}")

# --- 3. PREPARAZIONE TRANSAZIONE ---
try:
    # Converti il cognome in formato esadecimale (bytes)
    data_hex = w3.to_hex(text=COGNOME)

    # Prendi il 'nonce' (contatore delle transazioni del tuo account)
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    
    # Stima il costo del gas
    gas_price = w3.eth.gas_price

    # ID della chain Sepolia (è 11155111)
    chain_id = w3.eth.chain_id

    # Costruisci la transazione
    tx = {
        'to': MY_ADDRESS,          # Inviamo a noi stessi
        'value': w3.to_wei(0, 'ether'), # 0 ETH
        'gas': 100000,             # Limite gas (sufficiente per i dati)
        'gasPrice': gas_price,
        'nonce': nonce,
        'data': data_hex,           # Il cognome in esadecimale
        'chainId': chain_id
    }

    print(f"Sto preparando la transazione con data: {COGNOME} ({data_hex})")

    # --- 4. FIRMA E INVIO ---
    
    # Firma la transazione con la chiave privata
    signed_tx = w3.eth.account.sign_transaction(tx, MY_PRIVATE_KEY)

    print("Transazione firmata. Invio in corso...")

    # Invia la transazione firmata alla rete
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    # Ottieni l'hash della transazione (l'ID)
    tx_hash_hex = w3.to_hex(tx_hash)
    print(f"Transazione inviata! Hash (ID): {tx_hash_hex}")

    # --- 5. ATTESA CONFERMA ---
    print("In attesa della conferma (mining)...")
    
    # Aspetta che la transazione sia inclusa in un blocco
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
    
    print("\n--- CONFERMATA! ---")
    print(f"Inclusa nel blocco numero: {tx_receipt.blockNumber}")
    print(f"Gas utilizzato: {tx_receipt.gasUsed}")
    print(f"Puoi vederla sull'explorer: https://sepolia.etherscan.io/tx/{tx_hash_hex}")

except Exception as e:
    print(f"\nErrore durante l'invio della transazione:")
    print(e)