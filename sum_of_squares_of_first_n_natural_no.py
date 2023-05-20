def sumOfSquares(n) :
    if n < 0:
        pass
    sum = n * (n + 1) * (2 * n + 1) / 6
    return int(sum)

n = int(input('Enter n : '))
sum = sumOfSquares(n)
print(sumOfSquares(n))