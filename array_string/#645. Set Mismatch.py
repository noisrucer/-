class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repetition_sum = sum(nums)
        loss_sum = sum(set(nums))

        total_sum = 0

        res = []
        
        for i in range(1, len(nums) + 1):
            total_sum += i

        res.append(repetition_sum - loss_sum)
        res.append(total_sum - loss_sum)
        
        return res