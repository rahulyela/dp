# Python3 program to implement
# the above approach

# Function to find the length of
# longest subarray whose product
# is positive
def maxLenSub(arr, N):
	
	# Stores the length of current
	# subarray with positive product
	Pos = 0

	# Stores the length of current
	# subarray with negative product
	Neg = 0

	# Stores the length of the longest
	# subarray with positive product
	res = 0

	for i in range(N):
		if (arr[i] == 0):

			# Reset the value
			Pos = Neg = 0

		# If current element is positive
		elif (arr[i] > 0):

			# Increment the length of
			# subarray with positive product
			Pos += 1

			# If at least one element is
			# present in the subarray with
			# negative product
			if (Neg != 0):
				Neg += 1

			# Update res
			res = max(res, Pos)

		# If current element is negative
		else:
			Pos, Neg = Neg, Pos

			# Increment the length of subarray
			# with negative product
			Neg += 1

			# If at least one element is present
			# in the subarray with positive product
			if (Pos != 0):
				Pos += 1

			# Update res
			res = max(res, Pos)
			
	return res

# Driver Code
if __name__ == '__main__':
	
	arr = [ -1, -2, -3, 0, 1 ]
	N = len(arr)
	
	print(maxLenSub(arr, N))

# This code is contributed by mohit kumar 29
