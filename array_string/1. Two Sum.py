class Solution:
    # O(log n)
    def binary_search_recursion(self, target, start, end, data, base_index=None):
        if start > end:
            return None

        mid = (start + end) // 2

        if data[mid] == target and base_index != mid:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

        return self.binary_search_recursion(target, start, end, data, base_index)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_list = sorted(nums)
        length = len(nums)
        answer = []
        response = []

        # O(n)
        for i in range(length):
            # O(log n)
            j = self.binary_search_recursion(
                target-sorted_list[i], 0, length-1, sorted_list, base_index=i)
            if j:
                answer = [i, j]
                break

        if answer:
            # O(n)
            print(answer)
            for i in range(length):
                if nums[i] == sorted_list[answer[0]]:
                    response.append(i)
                    break
            # O(n)
            for i in range(length-1, -1, -1):
                if nums[i] == sorted_list[answer[1]]:
                    response.append(i)
                    break

        return response
