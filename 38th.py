import pickle


def read(filename):
    m = filename[:-4]
    if m.isalnum():  # FILE NAME SHOULD IN STRING FORMAT
        if filename[-4:] == ".bat":  # FOR BINARY FILE READING
            mode = "rb"
            try:
                f = open(f"{filename}", f"{mode}")
                k = pickle.load(f)
                for i in k:
                    print(i)
                f.close()
            except:
                # IF FILE NOT PRESENT IT SHOWAS AN ERROR
                print("File Not Found")


def write(filename, list):
    m = filename[:-4]
    if m.isalnum():  # FILE NAME SHOULB IN STRING FORMAT
        if filename[-4:] == ".bat":  # FOR BINARY FILE READING
            mode = "wb"
            try:
                f = open(f"{filename}", f"{mode}")
                k = pickle.dump(list, f)
                f.close()
                print("Sucessfully Written Data in bindary file")
            except:
                # IF FILE NOT PRESENT IT SHOWAS AN ERROR
                print("File Not Found")


def append(filename, list):
    m = filename[:-4]
    if m.isalnum():  # FILE NAME SHOULB IN STRING FORMAT
        if filename[-4:] == ".bat":  # FOR BINARY FILE READING
            mode = "ab"
            try:
                f = open(f"{filename}", f"{mode}")
                k = pickle.dump(list, f)
                f.close()
                print("Sucessfully Written Data in bindary file")
            except:
                # IF FILE NOT PRESENT IT SHOWAS AN ERROR
                print("File Not Found")


def search(filename):
    m = filename[:-4]
    if m.isalnum():  # FILE NAME SHOULB IN STRING FORMAT
        if filename[-4:] == ".bat":  # FOR BINARY FILE SEARCHING
            mode = "rb"
            try:
                f = open(f"{filename}", f"{mode}")
                k = pickle.load(f)
                n = input("Enter RollNo : ")+" "
                for i in k:
                    if i[0]==n:
                        v=i
                        s=1
                        break
                    else:
                        s=0
                if s==1:
                    print(v)
                else:
                    print("No Data Found..")
            except:
                # IF FILE NOT PRESENT IT SHOWAS AN ERROR
                print("File Not Found")

#OPTIONAL PART
while True:
    s=input("1.Read Binary File\n2.Write Binary File\n3.Append Binary File\n4.Search Binary File\n5.Exit\nEnter Your Choice : ")
    if s=="1":
        read("test.bat")
    elif s=="2":
        ml=[]
        for i in range(int(input("Enter Number of Students : "))):
            l=[0,0,0]
            rl=input("Enter Roll Number : ")+" "
            nm=input("Enter Name : ")+" "
            cl=input("Enter Class : ")+"\n"
            l[0],l[1],l[2]=rl,nm,cl
            ml.append(l)
        write("test.bat",ml)

    elif s=="3":
        ml=[]
        for i in range(int(input("Enter Number of Students : "))):
            l=[0,0,0]
            rl=input("Enter Roll Number : ")+" "
            nm=input("Enter Name : ")+" "
            cl=input("Enter Class : ")+"\n"
            l[0],l[1],l[2]=rl,nm,cl
            ml.append(l)
        append("test.bat",ml)
    elif s=="4":
        search("test.bat")
    elif s=="5":
        print("Exiting...")
        break
    else:print("Invalid Syntax!!")