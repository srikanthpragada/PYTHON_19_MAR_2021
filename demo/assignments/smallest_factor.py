num = 24567

for i in range(2, num//2 + 1):
    if num % i == 0:
        print(i)
        break
else:
    print(num)

