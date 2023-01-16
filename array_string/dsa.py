digits = [4,3,2,1]

for idx in range(len(digits)-1, -1, -1):
    if digits[idx] != 9:
        print(digits[idx] + 1)
    elif len(digits) == 1:
        digits[idx] == 1
        digits.append(0)
    else:
        digits[idx] = 0
        