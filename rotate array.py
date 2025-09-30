#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        if n == 0:
            return
    
        # Handle cases where d is larger than the array length
        d = d % n
        
        # Perform the in-place rotation
        arr[:] = arr[d:] + arr[:d]
        return arr
            
        
        
        
