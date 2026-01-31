class kQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.arr = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        
        # Initialize the free list: 
        # Each index points to the next index, creating a chain of empty slots.
        self.next = [i + 1 for i in range(n)]
        self.next[n - 1] = -1  # Last slot has no "next"
        self.free_top = 0

    def isFull(self):
        # If free_top is -1, there are no available slots in the array.
        return self.free_top == -1

    def isEmpty(self, i):
        # If the front of the i-th queue is -1, it's empty.
        return self.front[i] == -1

    def enqueue(self, x, i):
        if self.isFull():
            return False
        
        # 1. Grab the first available index from the free list
        insert_at = self.free_top
        
        # 2. Update free_top to the next available slot
        self.free_top = self.next[insert_at]
        
        # 3. If queue i is empty, set the front
        if self.isEmpty(i):
            self.front[i] = insert_at
        else:
            # Link the old rear to the new element
            self.next[self.rear[i]] = insert_at
            
        # 4. Update the rear and the next pointer of the new element
        self.next[insert_at] = -1
        self.rear[i] = insert_at
        
        # 5. Store the data
        self.arr[insert_at] = x
        return True

    def dequeue(self, i):
        if self.isEmpty(i):
            return -1
        
        # 1. Find the index of the front element
        dequeue_idx = self.front[i]
        
        # 2. Update the front to the next element in queue i
        self.front[i] = self.next[dequeue_idx]
        
        # 3. If the queue becomes empty, reset the rear
        if self.front[i] == -1:
            self.rear[i] = -1
            
        # 4. Add the now-empty slot back to the free list
        self.next[dequeue_idx] = self.free_top
        self.free_top = dequeue_idx
        
        return self.arr[dequeue_idx]

