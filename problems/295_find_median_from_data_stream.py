'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
'''

from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        maxHeap = self.maxHeap
        minHeap = self.minHeap
        heappush(maxHeap, -num)
        heappush(minHeap, -heappop(maxHeap))

        if len(maxHeap) < len(minHeap):
            heappush(maxHeap, -heappop(minHeap))

    def findMedian(self) -> float:
        maxHeap = self.maxHeap
        minHeap = self.minHeap
        if len(maxHeap) > len(minHeap):
            return -maxHeap[0]
        else:
            return (minHeap[0] + -maxHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        nums = self.nums
        l = len(nums)
        if l % 2 == 0:
            return (nums[l//2] + nums[l//2 - 1])/2
        else:
            return nums[l//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
