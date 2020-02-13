# Python program to count and 
# print all palindrome numbers in a list. 

def palindromeNumbers(list_a): 

	c = 0

	# loop till list is not empty 
	for i in list_a:			 

		# Find reverse of current number 
		t = i 
		rev = 0
		while t > 0: 
			rev = rev * 10 + t % 10
			t = t / 10

		# compare rev with the current number 
		if rev == i: 
			printi,
		c = c + 1

	
	print( "Total palindrome nos. are", c )
	

# Driver code 
def main(): 

	list_a = [10, 121, 133, 155, 141, 252,222,123,2211,1212,456,433] 
	palindromeNumbers(list_a) 

						 

		 # main function call 
