'''
1. 중복되는 숫자 중 가장 많이 중복되는 숫자의 개수를 찾는다.
    1-1. 중복되는 숫자의 개수가 동일하고 여러 요소가 있다면 ?
    
2. 그 요소를 기점으로 오른쪽 왼쪽을 제거하면서 가장 작은 길이가 될 때까지 반복한다.
'''

nums = [1,2,2,3,1,4,2]

idx_table = dict()
val_table = dict()


temp = 0

for idx, val in enumerate(nums):
    if val in idx_table:
        idx_table[val] = idx - idx_table[val]
        val_table[val] += 1
    else:
        idx_table[val] = idx
        val_table[val] = 1
        
print(idx_table)
print(val_table)