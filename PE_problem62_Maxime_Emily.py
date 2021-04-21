'''
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube 
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

from itertools import permutations

def is_perfect_cube(x):
    x = abs(x)
    return int(round(x ** (1. / 3))) ** 3 == x


#perm = permutations(list(123))
print(type(list(str(123))))
print(list(str(123)))

numberOfCubes = 0
ourNumber = 1

while numberOfCubes !=3 :
    numberOfCubes = 0
    Solution = set()
    listOfDigits = list(str(ourNumber**3))
    setOfPermutations = set(permutations(listOfDigits))

    for perm in setOfPermutations:
        if perm[0] != '0':
            PermutedNumber = int(''.join(perm))
            if is_perfect_cube(PermutedNumber):
                Solution.add((int(round(PermutedNumber**(1./3))),PermutedNumber))    
    numberOfCubes = len(Solution)
    ourNumber += 1

print(Solution)

#for i in perm:
#    print(i)

#Function producing the list of all permutation of a number

