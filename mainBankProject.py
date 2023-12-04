banks = ["SBI","PNB","ICICI","UBI","World Bank"]
balance = [5000,10000,15000,20000,25000]
accNums = [24100122038,24100122028,24100122047,24100122011,24100122051]
cardNums = {38:[0,123,1129],
            28:[1,123,1129],
            47:[2,123,1129],
            11:[3,123,1129],
            51:[4,123,1129]}


def bankChoice(bankNum):
    accNo = int(input("Give your account number: "))
    if accNo == accNums[bankNum]:
        
        while True:
            print(f"---WELCOME TO {banks[bankNum]}---")
            print("Press 1 to Withdraw\nPress 2 to Deposite\nPress 3 to Check Balance")
            work = int(input("Give your choice: "))
            if work == 1:
                print("Your bank balance is",balance[bankNum])
                withdrawAmount = int(input("Give your withdraw Amount: "))
                if withdrawAmount <= balance[bankNum]:
                    balance[bankNum] -= withdrawAmount
                    print("Your bank balance is",balance[bankNum])
                else:
                    print("Insufficent Balance!!")
            elif work == 2:
                depositeAmount = int(input("Give your deposite Amount: "))
                balance[bankNum] += depositeAmount
                print("Your bank balance is",balance[bankNum])
            elif work == 3:
                print("Your bank balance is",balance[bankNum])
            else:
                print("Wrong Choice!!")
            x = (input("Want to continue? (Y/N): ")).upper()
            if x == "Y":
                pass
            else:
                print("Thank you for Choosing",banks[bankNum])
                break
    else:
        print("Wrong Credential!!")

def atmChoice(atmNum):
    print(f"Welcome to {banks[atmNum]} ATM")
    while True:
        cardNum = int(input("Give your debit card number: "))
        if cardNum in cardNums.keys():
            cvv = int(input("Give CVV: "))
            exp = int(input("Give Expiary year: "))
            data = cardNums[cardNum]
            if data[1] == cvv and data[2] == exp:
                print("Your bank balance is",balance[data[0]])
                withdrawAmount = int(input("Give your withdraw Amount: "))
                if withdrawAmount <= balance[data[0]]:
                    balance[data[0]] -= withdrawAmount
                    print("Your bank balance is",balance[data[0]])
                else:
                    print("Insufficent Balance!!")
            else:
                print("Wrong Credentials!!")
        else:
            print("USER NOT FOUND!!")
        x = (input("Want to continue? (Y/N): ")).upper()
        if x == "Y":
            pass
        else:
            print("Thank you for Choosing",banks[atmNum],"ATM")
            break
        


def bank():
    print("WELCOME")
    for i in range(len(banks)):
        print(f"Click {i+1} for {banks[i]}")
    bankNum = int(input("Give your choice: "))
    if bankNum > 0 and bankNum <= len(banks):
        bankChoice(bankNum - 1)
    else:
        print("Wrong Choice!!")
       
def ATM():
    print("WELCOME")
    for i in range(len(banks)):
        print(f"Click {i+1} for {banks[i]} ATM")
    bankNum = int(input("Give your choice: "))
    if bankNum > 0 and bankNum <= len(banks):
        atmChoice(bankNum - 1)
    else:
        print("Wrong Choice!!")


def main():
    while True:
        x = (input("Press 1 for bank\nPress 2 for ATM\nPress any number to Exit\nChoose number: "))
        if int(x) == 1:
            bank()
        elif int(x) == 2:
            ATM() #ATM
        else:
            break


if __name__ == "__main__":
    main()