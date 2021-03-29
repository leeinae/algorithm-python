s = list(input())
s.sort()
sum_value = 0
for i in s:
    if i.isalpha():
        print(i, end="")
    else:
        sum_value += int(i)
print(sum_value)
