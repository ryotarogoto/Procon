#!/usr/bin/env python

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())

def dfs(depth, sum_a):
    global n
    if (depth == n): return sum_a == k
    if (dfs(depth + 1, sum_a)): return True
    if (dfs(depth + 1, sum_a + a[depth])): return True
    return False

if __name__ == "__main__":
    if (dfs(0, 0)): print("Yes")
    else: print("No")

