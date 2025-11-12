from web3 import Web3

# Inizializza un'istanza web3 generica (non connessa)
w3 = Web3()

# Crea un nuovo account (chiave privata, chiave pubblica, indirizzo)
account = w3.eth.account.create()

# Estrai i dati
private_key = account.key.hex()
address = account.address

print(f"Account creato con successo!")
print(f"Indirizzo (Address): {address}")
print(f"CHIAVE PRIVATA (Private Key): {private_key}")
print("\n---")
print("IMPORTANTE: Salva questa CHIAVE PRIVATA in un luogo sicuro!")
print("NON condividerla MAI con nessuno.")
print("Usa l'INDIRIZZO (Address) per ricevere fondi dal faucet.")