# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     arr1 = ransomNote
    #     frequency_map1 = {}
    #     for num in arr1:
    # # get(num, 0) returns the current count or 0 if the key is missing
    #         frequency_map1[num] = frequency_map1.get(num, 0) + 1
    #     arr2 = magazine
    #     frequency_map2 = {}

    #     for num in arr2:
    #         frequency_map2[num] = frequency_map2.get(num, 0) + 1

    #     for k,v in frequency_map1.items():
    #         for k1,v1 in frequency_map2.items():
    #             if k == k1 and v <= v1:
    #                 return True
    #             else:
    #                 return False  
# from collections import Counter

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         # Time Complexity: O(M) + O(N) = O(M + N) 
#         # where M is the length of magazine and N is the length of ransomNote.
#         # Space Complexity: O(k), where k is the number of unique characters (at most 26).
        
#         # 1. Create a frequency map for the magazine
#         # Using Counter is the most idiomatic and efficient way in Python.
#         magazine_counts = Counter(magazine)
        
#         # 2. Iterate through the ransomNote and consume characters
#         for char in ransomNote:
#             # Check if the character exists AND if the count is greater than 0
#             if magazine_counts.get(char, 0) > 0:
#                 # Consume one instance of the character
#                 magazine_counts[char] -= 1
#             else:
#                 # Either the character is missing or we ran out of it
#                 return False
                
#         # 3. If the loop completes, all required characters were found
#         return True
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, '', 1)
            else:
                return False
        return True
