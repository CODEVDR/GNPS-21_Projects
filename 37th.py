"""37.	Write a menu driven program to perform read and write operation using a text file called “Student.txt” containing student roll_no, name and address using two separate functions as given below:
	Student_record(filename): Entering student details
While writing to a file (student.txt), the roll_no fiels will be separated from the remaining fields with a comma separator.
	Student_readdata(filename): Display student details
	Student_search(filename): Search a student on the basis of roll_no."""
# functions


def Student_record(filename):
    f = open(filename, "a")
    for i in range(int(input("Enter Number of Students : "))):
        l = [0, 0, 0]
        nm = input("Enter Your Name : ")
        rn = input("Enter Your Roll Number : ")
        add = input("Enter Your Address : ")
        l[0], l[1], l[2] = nm+" ", rn+" ", add+"\n"
        f.writelines(l)


def Student_readdata(filename):
    f = open(filename)
    f = f.read()
    print("NAME ROLL_NO ADDRESS")
    for i in f:
        print(i, end="")


def Student_search(filename):
    f = open(filename)
    # Adjusting Output
    f = f.read()
    f = f.split("\n")
    ml = []
    for i in f:
        l = []
        j = i.split()
        l.append(j)
        ml.append(l)
    ml.pop()
    # Searching Starts from here
    n = input("Enter Your Roll Number : ")
    for i in ml:
        if i[0][1] == n:
            s = i[0][0]+" "+i[0][1]+" "+i[0][2]
            v = 1
        else:
            v = 0
    if v == 0:
        print("No Data Found..")
    elif v == 1:
        print(s)


print("\t\t\t\tStudent Data")
s = input(
    "1.Student_record\n2.Student_readdata\n3.Student_search\nEnter Your Choice : ")
if s[0] == "1":
    Student_record("Students.txt")
elif s[0] == "2":
    Student_readdata("Students.txt")
elif s[0] == "3":
    Student_search("Students.txt")
else:
    print("Invalid Syntax")
