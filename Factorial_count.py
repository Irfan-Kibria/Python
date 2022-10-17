a = int(input())

varriable = 1

if a<0:
    print("Number Must be Positive")

elif a==0:
    print("Factorial of 0 is: 1")

else:
    for i in range(1, a+1):
        varriable = varriable*i
print(f"factorial of {a}:",varriable )