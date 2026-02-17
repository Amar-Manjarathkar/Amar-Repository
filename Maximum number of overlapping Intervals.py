class Solution:
    def overlapInt(self, arr):
        events = []
        
        for s, e in arr:
            events.append((s, 1))      # start event
            events.append((e+1, -1))   # end event (exclusive)
        # print(events)
        events.sort()
        
        curr = 0
        max_overlap = 0
        
        for _, val in events:
            curr += val
            max_overlap = max(max_overlap, curr)
            
        return max_overlap
