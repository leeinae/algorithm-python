num = input()

total = int(num[0])
for i in num[1:]:
    temp = int(i)

    if total * temp > total + temp:
        total *= temp
    else:
        total += temp

print(total)