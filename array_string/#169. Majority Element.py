class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = defaultdict(int)

        for num in nums:
            dct[num] += 1

        for items in dct.items():
            if items[1] >= (len(nums)/2):
                return items[0]