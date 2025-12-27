#PINupdate.py
import pickle
def pinupdate():
    with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data","rb")as fp:
        records=list()
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    found=False
    acno=int(input("Enter ur account number to update pin:"))
    for index in range(len(records)):
         if (records[index][0]==acno):
             found=True
             recindex=index
             break
    if(found):
         newPIN=float(input("Enter  new 4 digit pin:"))
         records[recindex][3]=newPIN
         with open("C:\\Users\\pc\\PycharmProjects\\MYPROJECT\\cuspro.data","wb")as fp:
             for record in records:
                pickle.dump(record, fp)
         print("\tcustomer PIN updated varify!:")
    else:
         print("\tEmployee Does not exit")
# pinupdate()












