'''
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube 
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

def dictionaryOfDigits(ourNumber):
    ourDictionary = {}
    for digit in str(ourNumber):
        ourDictionary[digit] = ourDictionary.get(digit,0) + 1
    return ourDictionary

def orderedDigits(ourNumber):
    listToOrder = list(str(ourNumber))
    listToOrder.sort()
    solution = ''.join(listToOrder)
    return solution

#We will create a dictionary keeping all the cubes that we have with the number of times they appear as a cube
DictionaryOfCubes = {}
ourNumber = 1
currentLength = 0
maxLength = currentLength
lengthNotFound = True
numberOfCubedPermutations = 5
digitsOfNumber  = {}
listOfSolutions = []
smallestSolution = 0



while currentLength <= maxLength:
    ourNumberCubed = ourNumber**3
    currentLength = len(str(ourNumberCubed))
    digitsOfNumber = orderedDigits(ourNumberCubed)
    
    if DictionaryOfCubes.get(digitsOfNumber,0) == 0 :
        DictionaryOfCubes[digitsOfNumber] = [(ourNumber,ourNumberCubed)]
    else:
        DictionaryOfCubes[digitsOfNumber].append((ourNumber,ourNumberCubed))


    
    #print((digitsOfNumber,DictionaryOfCubes[digitsOfNumber]))
    
    #We look how many elements cubed give you the digitsOfNumber    
    if len(DictionaryOfCubes[digitsOfNumber]) == numberOfCubedPermutations:
        maxLength = currentLength
        lengthNotFound = False
        listOfSolutions.append(DictionaryOfCubes[digitsOfNumber])
    elif len(DictionaryOfCubes[digitsOfNumber]) == numberOfCubedPermutations+1:

        listOfSolutions.remove(DictionaryOfCubes[digitsOfNumber])
        
        if len(listOfSolutions) == 0:
            maxLength = currentLength
            lengthNotFound = True
    elif lengthNotFound :
        maxLength = currentLength
    ourNumber += 1

for solution in listOfSolutions:
    if smallestSolution == 0 or smallestSolution > solution[0][1]:
        smallestSolution = solution[0][1]
    


print(smallestSolution)



