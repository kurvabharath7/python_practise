num = int(input("enter the number"))

if num <= 1:
    print("not prime")

for i in range(2, num):
    if num % i == 0:
        print("not prime")
        break;
else:
    print("number is prime")

