
import heapq
class Solution:
    def kthElement(self, a, b, k):
        # code here
        merge = list(heapq.merge(a,b))
        return merge[k-1]
