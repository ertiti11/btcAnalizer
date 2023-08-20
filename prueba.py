import requests
import time

# API URL
BASE_URL = "https://blockchain.info/"

# Dirección de billetera de origen
wallet_address = "TU_DIRECCION_DE_BILLETERA"

# Función para obtener transacciones OUT de una dirección
def get_out_transactions(address):
    url = f"{BASE_URL}rawaddr/{address}"
    response = requests.get(url)
    data = response.json()
    out_transactions = []

    for tx in data.get("txs", []):
        for output in tx["out"]:
            if "spent" in output and output["spent"] == False:
                out_transactions.append(output["addr"])

    return out_transactions

# Función para obtener las transacciones OUT de una lista de direcciones con una profundidad dada
def get_all_out_transactions_with_depth(address_list, depth):
    if depth == 0:
        return {}

    all_out_transactions = {}

    for address in address_list:
        out_transactions = get_out_transactions(address)
        all_out_transactions[address] = get_all_out_transactions_with_depth(out_transactions, depth - 1)
        time.sleep(2)  # Espera 2 segundos antes de la siguiente petición

    return all_out_transactions

def print_tree(tree, indent=0):
    for address, sub_tree in tree.items():
        print("  " * indent + f"Dirección: {address}")
        if sub_tree:
            print_tree(sub_tree, indent + 1)

if __name__ == "__main__":
    wallet_addresses = ["DIRECCION_1", "DIRECCION_2", "DIRECCION_3"]  # Agrega las direcciones que desees
    max_depth = 3  # Profundidad máxima de exploración

    all_transactions_tree = get_all_out_transactions_with_depth(wallet_addresses, max_depth)
    print("Árbol de transacciones OUT:")
    print_tree(all_transactions_tree)
