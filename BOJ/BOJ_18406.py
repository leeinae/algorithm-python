n = input()
str_len = len(n)

sum_str = 0
for i in range(str_len):
    if i > (str_len // 2) - 1:
        sum_str -= int(n[i])
    else:
        sum_str += int(n[i])
if sum_str == 0:
    print("LUCKY")
else:
    print("READY")
