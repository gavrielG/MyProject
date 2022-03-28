number=int(input("enter number:"))
right=number%10
left=number//100
middle=number//10%10

while 100<=number<=999:
    print(right+left+middle)
    number = int(input("enter number:"))
print("invalid number")




age=int(input("your age is"))

while 0<=age<=120:
    if 0<=age<=18:
        print("child")
        age = int(input("your age is"))
    if 19<=age<=60:
        print("adult")
        age = int(input("your age is"))
    if 61<=age<=120:
        print("senior")
        age = int(input("your age is"))
print("invalid age")


print("#########################################################")



num1=int(input("first number :"))
num2=int(input("second number :"))



while num1%2==0 and num2%2==0:
    print(num1+num2)
    num1 = int(input("first number :"))
    num2 = int(input("second number :"))
if num1%2>0:
    print(num1*num2)

print("##################################")

number1=int(input("first number:"))
number2=int(input("second number:"))

while number1+number2==10:
    print("sum is 10")
    number1 = int(input("first number:"))
    number2 = int(input("second number:"))
if number1+number2==12:
    print("Error 404")

print("##########################################")


num=int(input("insert number here:"))

while 10<=num<=99:
    if 10 <= num <= 99 and num % 7 == 0 or num % 10 == 7 or num // 10 == 7:
        print("its your lucky number !!")
        num = int(input("insert number here:"))
    else:
        print("its not your lucky number")
        num = int(input("insert number here:"))
if num>99:
   print("yalla nigmar")








