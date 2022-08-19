from csv import *
def Salary():
    f=open("Employee.csv","a+",newline="")
    s=input("Do You Want To Write Header : ").upper()
    if s=="Y":
        writer(f).writerow(["Emp_Code","Name","Grade","Salary"])
    ml=[]
    for i in range(int(input("Enter Number of Employees : "))):
        Emp_Code=input("Enter Employee Code : ")
        Name=input("Enter Employee Name : ")
        Grade=input("Enter Employee Grade : ")
        Salary=input("Enter Employee Salary : ")
        ml.append([Emp_Code,Name,Grade,Salary])
    writer(f).writerows(ml)
#Salary()
print("Printing Data Of Employess Whose Salary is 40000 or mode")
f=open("Employee.csv")
f=reader(f)
j=0
print("Emp_Code","Name","Grade","Salary")
for i in f:
    if j!=0:
        if int(i[3])>=40000:
            print(i[0],i[1],i[2],i[3])
    j+=1