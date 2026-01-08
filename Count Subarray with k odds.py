from collections import defaultdict

class Solution:
    def countSubarrays(self, arr, k):
        # Dictionary to store frequency of prefix odd counts
        # Initialize with 0: 1 to handle subarrays starting from index 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        
        current_odd_count = 0
        total_subarrays = 0
        
        for num in arr:
            # Increment count if the number is odd
            if num % 2 != 0:
                current_odd_count += 1
            
            # If (current_odd_count - k) exists in our map, 
            # it means we found subarrays with exactly k odd numbers
            if (current_odd_count - k) in prefix_counts:
                total_subarrays += prefix_counts[current_odd_count - k]
            
            # Update the map with the current running count
            prefix_counts[current_odd_count] += 1
            
        return total_subarrays
