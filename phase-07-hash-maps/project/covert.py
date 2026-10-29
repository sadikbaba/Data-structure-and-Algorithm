# from this o(n^2)
def attach_usernames(accounts, transactions):
    result = []

    for txn in transactions:
        for account in accounts:
            if txn["user_id"] == account["user_id"]:
                result.append({
                    "transaction_id": txn["id"],
                    "username": account["username"]
                })
                break

    return result


# to this O(n)
def attach_usernames_convert(accounts, transactions):
    # Build lookup: user_id → username  (O(m))
    user_lookup = {account["user_id"]: account["username"] for account in accounts}

    result = []
    for txn in transactions:                          # O(n)
        username = user_lookup.get(txn["user_id"])    # O(1) average
        if username is not None:
            result.append({
                "transaction_id": txn["id"],
                "username": username,
            })
    return result


if __name__ == "__main__":
    accounts = [
        {"user_id": 10, "username": "amina"},
        {"user_id": 20, "username": "yusuf"},
        {"user_id": 30, "username": "zainab"},
    ]
    
    transactions = [
        {"id": "TX1", "user_id": 20},
        {"id": "TX2", "user_id": 10},
        {"id": "TX3", "user_id": 30},
    ]

    print(attach_usernames_convert(accounts, transactions))