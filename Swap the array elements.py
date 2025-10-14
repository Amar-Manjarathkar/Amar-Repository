class Solution:
	def swapElements(self, arr):
	    #Code here
	    for i in range(len(arr)-2):
	        arr[i], arr[i+2] = arr[i+2], arr[i]
	    
	    return arr
