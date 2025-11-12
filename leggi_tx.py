from web3 import Web3
import os
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# --- CONFIGURAZIONE ---
SEPOLIA_ENDPOINT_URL = os.getenv('SEPOLIA_ENDPOINT_URL')
TX_HASH_DA_LEGGERE = os.getenv('TX_HASH_DA_LEGGERE')

# Verifica che le variabili siano state caricate
if not SEPOLIA_ENDPOINT_URL or not TX_HASH_DA_LEGGERE:
    print("Errore: Assicurati di aver creato il file .env con SEPOLIA_ENDPOINT_URL e TX_HASH_DA_LEGGERE.")
    print("Usa .env.example come template.")
    exit() 

# --- CONNESSIONE ---
w3 = Web3(Web3.HTTPProvider(SEPOLIA_ENDPOINT_URL))

if not w3.is_connected():
    print("Errore: Impossibile connettersi.")
    exit()

print("Connesso. Recupero transazione...")

try:
    # --- LETTURA ---
    tx_data = w3.eth.get_transaction(TX_HASH_DA_LEGGERE)

    # Estrai il campo 'input' (contiene i dati della transazione)
    data_hex = tx_data.input
    
    # Converti HexBytes in stringa esadecimale
    data_hex_str = w3.to_hex(data_hex)

    # Decodifica i dati da esadecimale a testo (UTF-8)
    cognome_letto = w3.to_text(hexstr=data_hex_str)

    print("\n--- TRANSAZIONE TROVATA ---")
    print(f"Da: {tx_data['from']}")
    print(f"A: {tx_data.to}")
    print(f"Valore: {w3.from_wei(tx_data.value, 'ether')} ETH")
    print(f"Dati (Hex): {data_hex}")
    print(f"Dati (Testo): '{cognome_letto}'")

except Exception as e:
    print(f"\nErrore durante la lettura della transazione:")
    print(e)
    print("Verifica che l'HASH sia corretto e che la transazione sia stata minata.")