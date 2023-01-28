a = "0"
b = "0"

res = 0
ans = []


for i in range(len(a) - 1, -1, -1):
    res += (2 ** i) * int(a[len(a) - 1 - i])
    
    
for i in range(len(b) - 1, -1, -1):
    res += (2 ** i) * int(b[len(b) - 1 - i])

if res == 0:
    print(0)

while res != 1:
    remainder = res % 2
    res //= 2
    if res == 1 or res == 0:
        ans.append(res)
        res = 1
    else:
        ans.append(remainder)    
        
s = ""
    
for i in range(len(ans) - 1, -1, -1):
    s += str(ans[i])
    
print(s)