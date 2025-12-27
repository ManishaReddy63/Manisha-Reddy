#CusDeposite
from bankexcept import WithDrawError, InSuffFoundError, DepositeError
import pickle
def deposit():
    with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data", "rb") as fp:
        records = []
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    Acno = int(input("Enter the account num you want to deposit: "))
    found = False
    for index in range(len(records)):
        if records[index][0] == Acno:
            found = True
            break
    if found:
        bal = records[index][2]
        damt = int(input("Enter deposit amount:"))
        try:
            if damt <= 0:
                raise DepositeError
        except DepositeError:
            print("\tDon't try to deposit -ve / zero value-try again")
        except ValueError:
            print("\tDon't try to deposit alnums,strs and symbols-try again")
        else:
            bal = bal + damt
            print("\tUR Account xxxxxxxxx123 Credited by INR:{}".format(damt))
            print("\tUR Account xxxxxxxxx123  Balance after Deposit INR:{}".format(bal))
            records[index][2] = bal
            with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data", "wb") as fp:
                for record in records:
                    pickle.dump(record, fp)
                print("✅ Record updated successfully!")
    else:
        print("Customer not registered yet!")
def withdraw():
    with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data", "rb") as fp:
        records = []
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    Acno = int(input("Enter the account num you want to withdraw: "))
    found = False
    for index in range(len(records)):
        if records[index][0] == Acno:
            found = True
            break
    if found:
        bal = records[index][2]
        wamt = int(input("Enter withdraw amount: "))
        try:
            if wamt <= 0:
                raise WithDrawError
            elif (wamt + 500) > bal:
                raise InSuffFoundError
        except WithDrawError:
            print("you can't withdraw because your balance is below 0!")
        except InSuffFoundError:
            print("you can't withdraw because withdraw amount is more than your balance!")
        else:
            bal = bal - wamt
            print("\tUR Account xxxxxxxxx123 Debited by INR:{}".format(wamt))
            print("\tUR Account xxxxxxxxx123  Balance after Withdraw INR:{}".format(bal))
            records[index][2] = bal
            with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data", "wb") as fp:
                for record in records:
                    pickle.dump(record, fp)
                print("✅ Record updated successfully!")
    else:
        print("Customer not registered yet!")

