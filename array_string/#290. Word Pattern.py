pattern = "abba"
s = "dog dog dog dog"

s = s.split()

hash_table = dict()

for i in range(len(pattern)):
    if pattern[i] in hash_table:
        if hash_table[pattern[i]] != s[i]:
            print(False)
    else:
        if s[i] != hash_table.values():
            hash_table[pattern[i]] = s[i]

print(hash_table)