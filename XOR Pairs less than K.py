class TrieNode:
    def __init__(self):
        # children[0] for bit 0, children[1] for bit 1
        self.children = [None, None]
        # Count of numbers passing through this node
        self.count = 0

class Solution:
    def cntPairs(self, arr, k):
        root = TrieNode()
        count = 0
        max_bits = 32  # Standard integer size, or max(arr).bit_length()
       
        for num in arr:
            # 1. Query the Trie: How many existing numbers form XOR < k with 'num'?
            count += self.query(root, num, k, max_bits)
           
            # 2. Insert 'num' into the Trie for future numbers to pair with
            self.insert(root, num, max_bits)
           
        return count

    def insert(self, root, num, max_bits):
        node = root
        for i in range(max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1

    def query(self, root, num, k, max_bits):
        node = root
        count = 0
        for i in range(max_bits - 1, -1, -1):
            if not node:
                break
           
            num_bit = (num >> i) & 1
            k_bit = (k >> i) & 1
           
            # Case 1: If k_bit is 1
            # We want (num_bit ^ x_bit) < 1.
            # If (num_bit ^ x_bit) == 0, then the result bit is 0, which is < 1.
            # This is definitely valid for this bit position, so we add all numbers
            # down that branch and continue looking for the "boundary" case.
            if k_bit == 1:
                # If we pick the same bit as num_bit, XOR is 0. 0 < 1, so these are all valid.
                if node.children[num_bit]:
                    count += node.children[num_bit].count
               
                # We continue down the OTHER branch (opposite bit) to see if we can get closer to k
                node = node.children[1 - num_bit]
               
            # Case 2: If k_bit is 0
            # We strictly need (num_bit ^ x_bit) to be 0 (so result bit is 0).
            # This forces us to move down the branch where x_bit == num_bit.
            else:
                node = node.children[num_bit]
               
        return count
