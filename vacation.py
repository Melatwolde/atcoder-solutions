def max_happiness(n, a, b, c):
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = [a[0], b[0], c[0]]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b[i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c[i]

    return max(dp[n-1])

n = int(input())
a, b, c = [], [], []
for _ in range(n):
    _a, _b, _c = map(int, input().split())
    a.append(_a)
    b.append(_b)
    c.append(_c)

print(max_happiness(n, a, b, c))
