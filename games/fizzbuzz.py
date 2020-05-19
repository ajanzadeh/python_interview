# Write a program that returns the numbers from N to M both inclusive. But for multiples of three give "Fizz" instead of the number and for the multiples of five give "Buzz". For numbers which are multiples of both three and five, give "FizzBuzz".
#
# INPUT int N Int M
#
# OUTPUT string sequence ^^ the resulting sequence using commas as separators between elements
#
# EXAMPLE Input 1,5 Output "1,2,Fizz,4,Buzz"

class Solution:

	def run(self, N, M):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		FizzBuzzlist = []
		for i in range(N, M+1):
		  if (i % 5 == 0) and (i % 3 ==0):
		  	FizzBuzzlist.append("FizzBuzz")
		  elif i % 3 == 0:
		    FizzBuzzlist.append("Fizz")
		  elif i % 5 == 0:
		   	FizzBuzzlist.append("Buzz")
		  else:
		  	FizzBuzzlist.append(i)

		sequence = ','.join(map(str,FizzBuzzlist))


		return sequence
