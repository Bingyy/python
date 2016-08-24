def digitSum(n):
    arr = []
    for i in range(10):
        arr[i] = n % 10
        n = n // 10
    sum = 0
    for i in range(10)
        sum+=arr[i]
    return sum
sum = digitSum(1000)

print sum