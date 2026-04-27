import csv
with open('student.csv','w',newline='') as n:
    wrt=csv.writer(n)
    wrt.writerow(['si','name','address','mobile','salary'])
    mul=(['1','shashi','bhpl','4940','25000'],['2','sai','wrgl','9440','15000'],['3','hari','sgrd','8520','24000'])
    wrt.writerows(mul)
    
#read
import csv
with open('student.csv','r') as p:
    r=csv.reader(p)
    for i in r:
        print(i)


#dictreader
import csv
with open('students.csv','r') as m:
    q=csv.DictReader(m)
    for x in q:
        print('')

#update
import csv
temp=[]
with open('students.csv','r') as m:
    r=csv.reader(m)
    for x in r:
        if x[0]==1:
            x[2]='63026'
        temp.append(x)
print(temp)


import csv
ls=[]
with open('students.csv','r') as x:
    r=csv.reader(x)
    for x in r:
        if x!=4:
            ls.append(x)
print(ls)