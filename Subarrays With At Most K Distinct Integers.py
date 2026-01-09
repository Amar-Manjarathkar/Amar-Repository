# class Solution:
#     def countAtMostK(self, arr, k):
#         # Code here
#         # window = arr[:k]
#         count = 0
#         for i in range(len(arr)):
#             for j in range(i,len(arr)):
#                 if len(set(arr[i:j+1])) <= k:
#                     count+=1
#                     # print(arr[i:j+1])
#         return count   
class Solution:
    def countAtMostK(self, arr, k):
        n = len(arr)
        count = 0
        left = 0
        freq = {}
        
        for right in range(n):
            # Add the current element to the frequency map
            freq[arr[right]] = freq.get(arr[right], 0) + 1
            
            # If distinct elements > k, shrink the window from the left
            while len(freq) > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            
            # All subarrays ending at 'right' and starting between 'left' and 'right' 
            # are valid because if a window has <= k distinct elements, 
            # any smaller window inside it also does.
            count += (right - left + 1)
            
        return count
