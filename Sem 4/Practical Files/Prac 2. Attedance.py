
att=()
start = True
while(start):
    name = input("Enter Your Name: ")
    roll = input("Enter Your Roll No: ")
    lecture = input("Enter the lecture which you have attended: ")
    attendance = input("Enter P for Present or Enter A for Absent: ")
    student = ("name : "+name+", roll: "+roll+ ", lecture attended :"+lecture)
    a=(name,roll,lecture,attendance)
    att += a
    request = int(input("Enter 1 to insert more data or Enter 2  to see the available data:"))
    if(request==1):
        start=True
    else:
            print(att)
            start=False 
