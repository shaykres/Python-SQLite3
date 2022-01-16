import sqlite3
import os
import sys
from _Repository import repo
from DTO import Hats,Orders,Supplier
     
def main(args):
    fileobject=open(args[3],"w+")
    repo.init()
    repo.create_tables()
    inputfilename = args[1]
    with open(inputfilename) as inputfile:
        lineNumbers=inputfile.readline()
        first_row=lineNumbers.split(',')
        numofHats=int(first_row[0])
        numofSupp=int(first_row[1])
        for line in inputfile:
            if(numofHats>0):
                line=line.rstrip()
                new_table_row=line.split(',')
                repo.hat.insert(Hats(new_table_row[0],new_table_row[1],new_table_row[2],new_table_row[3]))
                numofHats=numofHats-1
            elif(numofSupp>0):
                line=line.rstrip()
                new_table_row=line.split(',')
                repo.supplier.insert(Supplier(new_table_row[0],new_table_row[1]))
                numofSupp=numofSupp-1

    inputfileorder = args[2]
    counter=1
    with open(inputfileorder) as inputfile:
        for line in inputfile:
            line=line.rstrip()
            new_table_row=line.split(',')
            hat_id=repo._executeOrder(new_table_row[1])
            repo.order.insert(Orders(counter,new_table_row[0],hat_id))
            myorder=repo.myOrder(counter)
            fileobject.write(myorder[0]+","+myorder[1]+","+myorder[2]+"\n")
            counter=counter+1
            repo.hat.delete()
    
    fileobject.close()
    repo._close()
         
if __name__ == '__main__':
    main(sys.argv)
   