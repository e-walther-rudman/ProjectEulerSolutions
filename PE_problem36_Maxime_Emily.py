'''
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

#write function to convert base 10 numbers to base 2

def convertToBinary(number):
    binaryString = list(str(bin(number)))
    binaryOutput = binaryString[2:]
    return binaryOutput


#write function to check if a string is a palindrome

def checkIfPalindrome(numberAsString):
    reversedNumber = numberAsString.copy()
    reversedNumber.reverse()
    return(numberAsString == reversedNumber)

totalOfDoublePalindromes = 0

for index in range(1000000):
    if(checkIfPalindrome(list(str(index))) and checkIfPalindrome(convertToBinary(index))):
        totalOfDoublePalindromes = totalOfDoublePalindromes + index

print(totalOfDoublePalindromes)