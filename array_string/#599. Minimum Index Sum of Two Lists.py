class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_table = defaultdict(int)

        index_sum = len(list1) + len(list2)
        
        res = []

        for idx, val in enumerate(list1):
            hash_table[val] = idx

        for i in range(len(list2)):
            if list2[i] in hash_table:
                hash_table[list2[i]] += i
                if hash_table[list2[i]] < index_sum:
                    if not res:
                        res.append(list2[i])
                    else:
                        res.clear()
                        res.append(list2[i])
                    index_sum = hash_table[list2[i]]
                elif hash_table[list2[i]] == index_sum:
                    res.append(list2[i])

        return res