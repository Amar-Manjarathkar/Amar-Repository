class Solution:
    def findMoves(self, chairs, passengers):
        # code here
        chairs.sort()
        passengers.sort()
        count = 0
        for i in range(len(chairs)):
            count += abs(chairs[i] - passengers[i])
        return count
