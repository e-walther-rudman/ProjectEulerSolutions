#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.


LargestPalindrome = 0

for FirstNumber in range(100,1000):
    for SecondNumber in range(FirstNumber, 1000):
        NumberAsList = list(str(FirstNumber*SecondNumber))
        NumberAsListOriginal = NumberAsList.copy()
        NumberAsList.reverse()
        if NumberAsListOriginal == NumberAsList  and FirstNumber*SecondNumber >LargestPalindrome:
            LargestPalindrome = FirstNumber*SecondNumber

print(LargestPalindrome)

