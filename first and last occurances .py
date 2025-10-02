#User function Template for python3


class Solution:
    def find(self, arr, x):
        
        # code here
        n = len(arr)
        
        def binary_search(is_first):
            low,high = 0, n-1
            result=  -1
            while(low<= high):
                mid =(low+high) // 2
                if arr[mid] == x:
                    result = mid
                    if is_first:
                        high = mid -1
                        
                    else:
                        low = mid + 1
                        
                elif x < arr[mid]:
                    high = mid -1
                else:
                    low= mid + 1
            return result
                    
        first = binary_search(True)
        last = binary_search(False)
        return (first,last)
