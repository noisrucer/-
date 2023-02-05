class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        cur_sum, max_sum = 0, float('-inf')

        for end, val in enumerate(nums):
            cur_sum += val

            if end - start + 1 == k:
                max_sum = max(max_sum, cur_sum)
                cur_sum -= nums[start]

                start += 1
        
        return round(max_sum / k, 5)