cnp = "2990219469000"
print(len(cnp))
c = int(cnp[-1])
print(c)

VALIDATOR = "279146358279"

cifre = cnp[:12]
print(cifre)


rezultat = sum([ int(VALIDATOR[i]) * int(cifre[i])   for i in range(12) ])
print(rezultat)
rezultat = rezultat % 11
print(rezultat)

if rezultat < 10:
    if c != rezultat:
        print(False)

else:
    if c != 1:
        print(False)

print(True)