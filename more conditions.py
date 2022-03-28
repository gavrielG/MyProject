number=int(input("your number is:"))

if number%2==0:
    print("your number is even")
else:
    print("your number is odd")

##########################################3

num1=int(input("your number is:"))
num2=int(input("your number is:"))
num3=int(input("your number is:"))

if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num1 and num2>num3:
        print(num2)
    else:
        if num3>num1 and num3>num2:
            print(num3)

##########################################

pcnum=input("how much pc's u fixed today :")

if pcnum=="":
    pcnum=15
else:
    pcnum=int(pcnum)
    print(pcnum*2)
