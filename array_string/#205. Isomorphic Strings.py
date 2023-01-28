'''
1. 일반화
s와 t 두 개의 문자열이 주어졌을 때 그것이 동형인지 여부를 밥ㄴ환해라

- 조건
    - 해당 문자가 두 번이상 등장하는가?
        - 해당 문자가 같은 인덱스인가?

'''

s = "aaeaa"
t = "uuxyy"

hash_table = dict()

for i in range(len(s)):
    if s[i] in hash_table:
            if hash_table[s[i]] == t[i]:
                print(True)
    else:
        hash_table[s[i]] = t[i]

print(False)
print(hash_table)