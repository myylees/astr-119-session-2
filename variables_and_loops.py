import numpy as np	
def main():
	i = 0		#integer i and initialize i to 0
	n = 10		#integer n, with value 10
	x = 119.0	#float x with value 119
	
	# we can use numpy to declare arrays quickly
	
	y = np.zeros(n,dtype=float)	#declare 10 zeros as floats using np
	
	#we can iterate though the elements of y
	#by passing an index
	
	for i range(n):			#i in range [0,n-1]
		y[i] = 2 * float(i) + 1		#set y = 2i+1 as float
	
	#we can also simply iterate through an array
	for y_element in y:
		print(y_element)
		
#execute the main function
if __name__ == "__main__":
	main()
	
	Error in coding