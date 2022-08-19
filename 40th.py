from csv import reader
def Trip():
    f=open("Holidays.csv")
    rd=reader(f)
    for i in rd:
        print(i[0],i[1],i[2],i[3])
Trip()
