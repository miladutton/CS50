def main():
    amount_due = 50
    amount_inserted = 0
    valid_coins = [5, 10, 25]

    # Start the loop and get input
    while amount_inserted < amount_due:
        coin = int(input("Insert Coins: "))

        # Make sure the coin is valid and add it to the total amount
        if coin in valid_coins:
            amount_inserted += coin
            print(f"Amount Due: {amount_due - amount_inserted}")

        # Handle invalid coins
        else:
            print("Amount Due: 50")

    # Calculate change
    change_owed = amount_inserted - amount_due
    if change_owed < 0:
        change_owed = 0

    print(f"Change Owed: {change_owed}")

main()
