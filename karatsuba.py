import math
var1 = input()
var2 = input()

def karatsuba(num1,num2):
    if int(num1)<10 or int(num2) < 10:
        return int(num1) * int(num2)
    m = max(len(str(num1)),len(str(num2)))
    m2 = (m//2)
    a = int(num1) // 10 ** m2
    b = int(num1) % 10 ** m2
    c = int(num2) // 10 ** m2
    d = int(num2) % 10 ** m2
    
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    AplusBCPlusD = karatsuba((a+b),(c+ d))
    step4 = AplusBCPlusD - bd - ac
    prod  = ac * 10 **(2 * m2) + step4 * 10 ** m2 + bd
    return prod
    
    
    

ans = karatsuba(var1,var2)

print(ans)
#miltiply the input if it is a single  digit


