def func(num):
    maxi = 0
    while num > 0:
        current = num % 10
        if current > maxi:
            maxi = current
        num //= 10
    print("max value:", maxi)


num = int(input("enter the number "))
func(num)
