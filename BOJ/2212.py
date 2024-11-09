n = int(input())
k = int(input())
klist = list(map(int, input().split()))

if k >= n:
  print(0)
else:
  klist.sort()
  diff = [klist[x]-klist[x-1] for x in range(1, n)]
  diff.sort(reverse=True)
  print(sum(diff[k-1:]))
