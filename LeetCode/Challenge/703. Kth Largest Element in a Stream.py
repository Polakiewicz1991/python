from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        self.nums.reverse()

        return  self.nums[self.k]

import heapq
class KthLargestInternet:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Implement KthLargest class:
#
#     KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
#     int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
#
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4 -> [8,5,"4",3,2]
# kthLargest.add(5);   // return 5 -> [8,5,"5",4,3,2]
# kthLargest.add(10);  // return 5 -> [10,8,"5",5,4,3,2]
# kthLargest.add(9);   // return 8 -> [10,9,"8",5,5,4,3,2]
# kthLargest.add(4);   // return 8 -> [10,9,"8",5,5,4,4,3,2]

