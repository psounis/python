def factorial(n):
    print((5-n) * "\t" + "CALL factorial(" + str(n) + ")")
    if n == 1:
        print((5-n+1) * "\t" + "return 1")
        return 1
    else:
        print((5 - n+1) * "\t" + "return " + str(n) + "*factorial(" + str(n-1) + ")")
        fact = factorial(n-1)
        res = n*fact
        print((5 - n+1) * "\t" + "return " + str(n) + "*" + str(fact) )
        return res


factorial(5)