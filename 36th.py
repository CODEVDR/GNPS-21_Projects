#36.	WAP in python  to define a function remove() that accepts two filenames, and copies all lines that do not start with lowercase letter form the first file into the second.
def remove(filename1,filename2):
    f1=open(filename1)
    f1=f1.read()
    f1=f1.split("\n")
    l=[]
    for i in f1:
        try:
            if i[0].isupper():
                l.append(i+"\n")
        except:
            pass
    f2=open(filename2,"w")
    f2=f2.writelines(l)
    print(f"Writing Data... in {filename2}")
remove("file1.txt","file2.txt")