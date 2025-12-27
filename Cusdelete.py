#Cusdelete.py
import pickle
def cosdel():
    with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data", "rb") as fp:
        records=list()
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    found = False
    acno = int(input("Enter ur account number to delete number Delete:"))
    for index in range(len(records)):
        if (records[index][0] == acno):
            found = True
            recindex = index
            break
    if(found):
        del records[recindex]
        with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data","wb")as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tcustomer account deleted--verify")
    else:
        print("employee data doesn't exit")

