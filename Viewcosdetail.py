#Viewcosdetail.py
import pickle
def viewcosdetail():
    with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data", "rb") as fp:
        records=list()
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        acno=int(input("Enter customer Acno to View Detailas:"))
        found=False
        for record in records:
            if(record[0]==acno):
                found=True
                rec=record
                break
        if(found):
            print("-"*50)
            print("Costomer Acno:{}".format(rec[0]))
            print("costomer Name:{}".format(rec[1]))
            print("Costomer Bal:{}".format(rec[2]))
            print("_"*50)
        else:
            print("\t costomer Does not Exit")
import pickle
def viewallcosdetail():
    with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data", "rb") as fp:
        print("-"*50)
        print("\tacno\t\tcustname\t\tbal\tpin")
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            except EOFError:
                print("-"*50)
                break

