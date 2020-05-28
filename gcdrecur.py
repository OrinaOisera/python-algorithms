def gcdrecur(a,b):
    '''
     a, b : positive integers

     returns a positive integer , the gcd of a & b

    '''
    newval = min(a, b)
    newval1 = max(a,b)
    if newval == 0 :
        return newval1
    else:
         result = gcdrecur(newval, newval1%newval)
         print(result)
         return  result


gcdrecur(1071,462)
