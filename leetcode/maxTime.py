# Python3 implementation of the approach 
from collections import defaultdict 

# Function to return the updated frequency 
# map for the array passed as argument 
def getFrequencyMap(arr, n): 
	hashMap = defaultdict(lambda:0) 
	for i in range(n): 
		hashMap[arr[i]] += 1
		print(hashMap)
	return hashMap 
	
# Function that returns true if the passed 
# digit is present in the map after 
# decrementing it's frequency by 1 
def hasDigit(hashMap, digit): 
	
	# If map contains the digit 
	if hashMap[digit] > 0: 
	
		# Decrement the frequency of 
		# the digit by 1 
		hashMap[digit] -= 1
	
		# True here indicates that the 
		# digit was found in the map 
		return True
	
	# Digit not found 
	return False
	
# Function to return the maximum possible 
# time_value in 24-Hours format 
def getMaxtime_value(arr, n): 
	
	hashMap = getFrequencyMap(arr, n) 
	flag = False
	time_value = "" 
	
	# First digit of hours can be 
	# from the range [0, 2] 
	for i in range(2, -1, -1): 
		if hasDigit(hashMap, i) == True: 
			flag = True
			time_value += str(i) 
			break
	
	# If no valid digit found 
	if not flag: 
		return "-1"
	
	flag = False
	
	# If first digit of hours was chosen as 2 then 
	# the second digit of hours can be 
	# from the range [0, 3] 
	if(time_value[0] == '2'): 
		for i in range(3, -1, -1): 
			if hasDigit(hashMap, i) == True: 
				flag = True
				time_value += str(i) 
				break
	
	# Else it can be from the range [0, 9] 
	else: 
		for i in range(9, -1, -1): 
			if hasDigit(hashMap, i) == True: 
				flag = True
				time_value += str(i) 
				break
			
	if not flag: 
		return "-1"
	
	# Hours and minutes separator 
	time_value += ":"
	
	flag = False
	
	# First digit of minutes can be 
	# from the range [0, 5] 
	for i in range(5, -1, -1): 
		if hasDigit(hashMap, i) == True: 
			flag = True
			time_value += str(i) 
			break
		
	if not flag: 
		return "-1"
	
	flag = False
	
	# Second digit of minutes can be 
	# from the range [0, 9] 
	for i in range(9, -1, -1): 
		if hasDigit(hashMap, i) == True: 
			flag = True
			time_value += str(i) 
			break
		
	if not flag: 
		return "-1"
	
	# Return the maximum possible 
	# time_value 
	return time_value 
	
# Driver code 
if __name__ == "__main__": 
	
	arr = [1, 0, 0, 9] 
	n = len(arr) 
	print(getMaxtime_value(arr, n)) 
	
# This code is contributed by 
# Rituraj Jain 
