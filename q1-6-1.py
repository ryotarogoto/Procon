#!/usr/bin/env python

n = int(input("Number of stick:"))
a = list()
ans = 0

for i in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            len = a[i] + a[j] + a[k]
            max_len = max([a[i], a[j], a[k]])
            rest = len - max_len
            if (max_len < rest):
                ans = max([ans, len])

if ans != 0:
    print("%d" % (ans))
else:
    print("0")
