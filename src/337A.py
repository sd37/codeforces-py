# http://codeforces.com/problemset/problem/337/A
# Status = AC

n, m = map(int, input().split())
f = list(map(int, input().split()))

f.sort()

best = f[n - 1] - f[0]

for k in range(1, m - n + 1):
    best = min(best, f[k + n - 1] - f[k])

print(best)