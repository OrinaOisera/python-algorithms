x = int(input("Enter an integer: "))
ans = 0

while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print("nor a perfect cube")
else:
    if x < 0:
        ans = - ans
    print("the cube root of" + str(x) + " is " + str(ans))

