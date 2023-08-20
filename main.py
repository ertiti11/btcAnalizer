import requests

# Dirección de Bitcoin de interés
btc_address = '16V5uBv27hSGVudsc1zKkckPWmr4DrEGnN'

transactions_url = f'https://blockchain.info/rawaddr/{btc_address}'
res = requests.get(transactions_url)
transactions_data = res.json()



for key in transactions_data.keys():
    print(key)



def getOutTransactions(transactions_data):

    # Conjunto para almacenar direcciones únicas de salida
    unique_output_addresses = set()

    # Recorre todas las transacciones
    for tx in transactions_data.get('txs', []):
        for output in tx.get('out', []):
            if 'addr' in output:
                unique_output_addresses.add(output['addr'])

    # Imprime las direcciones únicas de salida
    # for addr in unique_output_addresses:
    #     print(addr)
    return unique_output_addresses



def getInputTransactions(transactions_data):
    # Conjunto para almacenar direcciones únicas de entrada
    unique_input_addresses = set()

    # Recorre todas las transacciones
    for tx in transactions_data.get('txs', []):
        for input in tx.get('inputs', []):
            prev_out = input.get('prev_out', {})
            if 'addr' in prev_out:
                unique_input_addresses.add(prev_out['addr'])

    return unique_input_addresses

def getBalance(transactions_data):
    balance = (transactions_data['total_received']/ 1e8)
    return balance

def get_total_sent(transactions_data):
    total_sent = 0

    # Recorre todas las transacciones
    for tx in transactions_data.get('txs', []):
        for input in tx.get('inputs', []):
            prev_out = input.get('prev_out', {})
            if 'value' in prev_out:
                total_sent += prev_out['value']

    return (total_sent/ 1e8)



def getTotalReceived(transactions_data):
    total_received = 0

    # Recorre todas las transacciones
    for tx in transactions_data.get('txs', []):
        for output in tx.get('out', []):
            if 'value' in output:
                total_received += output['value']

    return (total_received/ 1e8)

def get_top_sender_amounts_btc(transactions_data):
    sender_dict = {}

    # Recorre todas las transacciones
    for tx in transactions_data.get('txs', []):
        for input in tx.get('inputs', []):
            prev_out = input.get('prev_out', {})
            if 'addr' in prev_out and 'value' in prev_out:
                sender_addr = prev_out['addr']
                sender_value = prev_out['value']
                if sender_addr in sender_dict:
                    sender_dict[sender_addr] += sender_value
                else:
                    sender_dict[sender_addr] = sender_value

    # Ordena el diccionario por valor (mayor a menor)
    sorted_senders = sorted(sender_dict.items(), key=lambda x: x[1], reverse=True)

    # Convertir los valores a BTC
    sorted_senders_btc = [(sender, amount / 1e8) for sender, amount in sorted_senders]

    return sorted_senders_btc




def tree(adress):
    transactions_url = f'https://blockchain.info/rawaddr/{address}'
    res = requests.get(transactions_url)
    transactions_data = res.json()

    getOutTransactions(transactions_data)
    