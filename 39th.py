from csv import writer
f=open("Holidays.csv","a",newline="")
s=input("Do You Want To Create Header [Y/N]: ").upper()
if s=="Y":
    writer(f).writerow(["Type","Trip","Days","TourCost"])
ml=[]
for i in range(int(input("Enter Number of Employees : "))):
    l=[0,0,0,0]
    ty=input("Enter Type : ")
    tr=input("Enter Trip : ")
    ds=input("Enter Days : ")
    tc=input("Enter TourCost : ")
    l[0],l[1],l[2],l[3]=ty,tr,ds,tc
    ml.append(l)
k=writer(f)
k.writerows(ml)
