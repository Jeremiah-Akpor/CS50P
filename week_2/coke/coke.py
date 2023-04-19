def main():
    amount_due = 50
    while True:
        print("Amount Due: " + str(amount_due) )
        inserted_coin = int(input("Insert Coin: "))
        if inserted_coin in [25,10,5]:
            change_owed = amount_due - inserted_coin
            amount_due = change_owed
            if change_owed <= 0:
                change_owed *= -1
                print("Change Owed: " + str(change_owed)  )
                break



if __name__ == "__main__":
    main()