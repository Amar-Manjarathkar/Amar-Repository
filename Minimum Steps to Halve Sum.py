class Solution:
  def minOperations(self, arr):
    # code here
    if not arr:
        return 0
    org_sum = sum(arr)
    target = org_sum / 2
    cur_sum = org_sum
    if cur_sum <= target:
        return 0
    heap = [-x for x in arr]
    heapq.heapify(heap)
    
    ops = 0
    while cur_sum > target:
        largest = -heapq.heappop(heap)
        reduction = largest / 2
        cur_sum -= reduction
        heapq.heappush(heap, -(largest / 2))
        ops +=1
    return ops
