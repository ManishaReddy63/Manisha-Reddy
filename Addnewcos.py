#Addnewcos.py
import pickle
def isunique(acno):
    with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data","rb")as fp:
        records=list()
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    found=True
    for record in records:
        if(record[0]==acno):
            found=False
            break
    return found
def addnewcos():
    with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data","ab")as fp:
        try:
            print("-" * 50)
            acno=int(input("Enter customer acno:"))
            if(isunique(acno)):
                custname=input("Enter customer name:")
                bal=float(input("Enter customer balance:"))
                pin=int(input("Enter customer pin:"))
                lst = list()
                lst.append(acno)
                lst.append(custname)
                lst.append(bal)
                lst.append(pin)
                print("-"*50)
                pickle.dump(lst, fp)
                print("\t Customer Data saved already in file")
            else:
                print("\t Customer Data not saved in file")
        except ValueError:
            print("Don't Enter alnums,strs,and symbols for PIN,Acno")


