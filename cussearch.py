#cussearch.py
import pickle
def Cussrh():
    with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data","rb")as fp:
        records=list()
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        acno=int(input("Enter customer Acno to search:"))
        found=False
        for record in records:
            if(record[0]==acno):
                found=True
                break
        if(found):
            print("\t Coustomer found -valid Employee")
        else:
            print("\t coustomer not found")


