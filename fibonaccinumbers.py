def fib(x):
    print("this number is being called " + str(x) )
    if x == 1 or x == 0:
        return 1
    else:
        res =  fib(x-1) + fib(x-2)
        print(" fib " + str(x-1) + " +  fib " + str(x-2))
        return res


print(fib(4))

