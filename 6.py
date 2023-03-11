number = int(input())
result = 1

for i in range(1, number + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    result += 1 / fact

print(round(result, 5))
