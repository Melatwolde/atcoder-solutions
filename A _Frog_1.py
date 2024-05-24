def frog(n, h):
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + abs(h[i - 1] - h[i - 2]))
        if i > 2:
            dp[i] = min(dp[i], dp[i - 2] + abs(h[i - 1] - h[i - 3]))
    return dp[n]

n= int(input())
h = [int(i) for i in input().split()]
print(frog(n, h))
