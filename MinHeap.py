class MinHeap:
    def __init__(self):        
        pass
    # build a new heap from a list of keys
    def build_heap(self, keys):
        self.heap = keys
    
    # add a new item to the heap
    def insert(self, item):
        self.heap.append(item)

    # return the item with the minimum key value, removing the item from the heap
    def del_min(self):
        x = self.heap[0]
        del self.heap[0]
        return x
    
    # print the minimum heap on the screen
    def display(self):
        # while self.heap[0] != min(self.heap):
        for i in range(len(self.heap)-1,-1,-1):
            if i*2 >= len(self.heap)-1:
                # print(i)
                pass
            elif self.heap[i*2+2] < self.heap[i] or self.heap[i*2+1] < self.heap[i]:
                if self.heap[i*2+2] > self.heap[i*2+1]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[i*2+1]
                    self.heap[i*2+1] = temp
                else:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[i*2+2]
                    self.heap[i*2+2] = temp
            i -= 1
        print(self.heap)

heap = MinHeap()

heap.build_heap([9, 5, 6, 2, 3])
heap.display()
heap.display() # 要再跑一次才會完成initializeＱＱ

heap.insert(1)
heap.insert(7)
heap.display()

print(heap.del_min())
print(heap.del_min())
heap.display()