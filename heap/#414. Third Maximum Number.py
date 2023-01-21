'''
TC: O(n)
SC: O(1) since we're using constant-sized heap and set
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        min_heap = []
        heapq.heapify(min_heap)
        visit = set()

        for e in nums:
            if e in visit:
                continue

            heapq.heappush(min_heap, e)
            if len(min_heap) > 3:
                top = min_heap[0]
                heapq.heappop(min_heap)
                if top in visit:
                    visit.remove(top)

            visit.add(e)

        return min_heap[0] if len(min_heap) == 3 else min_heap[-1]
