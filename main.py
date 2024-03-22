def func(num):
    maxi = 0
    while num > 0:
        current = num % 10
        if current > maxi:
            maxi = current
        num //= 10
    print("max value:", maxi)

def func1(guestsAmount):
    cuts =  guestsAmount - 1
    print("cuts amount:", cuts)

num = int(input("enter the number "))
func1(num)
