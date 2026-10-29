def group_transactions(transactions):
    result = {}

    for txn in transactions:
        network = txn["network"]  
        txn_id = txn["id"]         

        if network not in result:
            result[network] = []  

        result[network].append(txn_id)

    return result


if __name__ == "__main__":
    transactions = [
        {"id": "T1", "network": "MTN"},
        {"id": "T2", "network": "Airtel"},
        {"id": "T3", "network": "MTN"},
        {"id": "T4", "network": "Glo"},
        {"id": "T5", "network": "Airtel"},
    ]
    print(group_transactions(transactions))