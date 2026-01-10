class Solution:
    def countSubstr(self, s, k):
        # Helper function to count substrings with at most 'diff' distinct characters
        def atMost(diff):
            if diff <= 0:
                return 0
            
            left = 0
            count = 0
            char_freq = {}
            distinct_count = 0
            
            for right in range(len(s)):
                # Add character to window
                char = s[right]
                char_freq[char] = char_freq.get(char, 0) + 1
                if char_freq[char] == 1:
                    distinct_count += 1
                
                # Shrink window if distinct characters exceed diff
                while distinct_count > diff:
                    left_char = s[left]
                    char_freq[left_char] -= 1
                    if char_freq[left_char] == 0:
                        distinct_count -= 1
                    left += 1
                
                # Number of substrings ending at 'right' is the window size
                count += (right - left + 1)
                
            return count

        return atMost(k) - atMost(k - 1)
