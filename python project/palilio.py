# Generate all palindromic numbers less than n 
# A Python program to generate palindromic numbers 
# less than n. 
def createPalindrome(inp, b, isOdd): 
	n = inp 
	palin = inp 

	# checks if number of digits is odd or even 
	# if odd then neglect the last digit of input in 
	# finding reverse as in case of odd number of 
	# digits middle element occur once 
	if (isOdd): 
		n = n / b 

	# Creates palindrome by just appending reverse 
	# of number to itself 
	while (n > 0): 
		palin = palin * b + (n % b) 
		n = n / b 
	return palin 

# Function to print decimal palindromic number 
def generatePalindromes(n): 

	# Run two times for odd and even length palindromes 
	for j in range(2): 
		# Creates palindrome numbers with first half as i. 
		# Value of j decided whether we need an odd length 
		# of even length palindrome. 
		i = 1
		while (createPalindrome(i, 10, j % 2) < n): 
			print (createPalindrome(i, 10, j % 2)), 
			i = i + 1

# Driver Program to test above function 
n = 104
generatePalindromes(n) 

#This code is contributed by Afzal Ansari 
