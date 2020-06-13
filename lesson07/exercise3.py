N = 100

evens = set()
for number in range(0,N+1,2):
    evens.add(number)
print(evens)

odds = set()
for number in range(1,N,2):
    odds.add(number)
print(odds)

multiples3 = set()
for number in range(0,N,3):
    multiples3.add(number)
print(multiples3)

primes = set()
for number in range(2, N+1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        primes.add(number)
print(primes)

set1 = evens | multiples3
print(set1)

set2 = odds & primes
print(set2)

set3 = primes - odds
print(set3)

set4 = primes ^ odds
print(set4)