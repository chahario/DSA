# Enter your code here. Read input from STDIN. Print output to 

import heapq
min_heap = []
t = int(input())
for i in range(t):
    li = list(map(int,input().strip().split()))
    if len(li)>1:
        a,b = li[0],li[1]
        if a==1:
            heapq.heappush(min_heap,int(b))
        elif a==2:
            temp = []
            while min_heap:
            
                t = heapq.heappop(min_heap)
                if t == int(b):
                    min_heap = min_heap + temp
                    heapq.heapify(min_heap) # since it is inplace operation 
                    break
                else:
                    temp.append(t)
    else:
        if min_heap:
            t = heapq.heappop(min_heap)
            print(t)
            heapq.heappush(min_heap,t)
        
                
        else:
            print(-1)
#heapq.heapify() is designed to convert a standard Python list into a heap in-place. It modifies the list passed to it and returns None. Assigning the result of heapq.heapify() to min_heap will set min_heap to None, breaking subsequent heap operations.
# This solution is not optimized as it uses a linear search to remove an element from the heap. 
# we can use a dictionary to keep track of the elements and their counts to optimize the removal operation.
'''
A common and efficient way to handle arbitrary deletions in a heap when using heapq is through lazy deletion. This involves:

Keeping the main heap (min_heap).
Using an auxiliary data structure (like a dictionary or counter) to keep track of elements that have been "marked" for deletion but are still present in the heap.
When accessing the minimum element (Type 3), you first check if the element at the top of the heap (min_heap[0]) is marked for deletion. If it is, you pop it and decrement its deletion count, repeating this process until the element at the top is not marked for deletion.
'''