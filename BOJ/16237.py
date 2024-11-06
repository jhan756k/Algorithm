num = list(map(int, input().split()))
num.insert(0, 0)
ans = num[5]+num[4]+num[3]
num[1] = max(0, num[1]-num[4])
a = num[2] - num[3]
num[2] = max(0, a)
num[3] = max(0, -a)
if num[3] > 0:
  num[1] = max(0, num[1] - (num[3]*2))
ans += num[2]//2
num[1] = max(0, num[1] - num[2]//2)
num[2] %= 2
if num[2] == 1:
  ans += 1
  num[1] = max(0, num[1]-3)
ans += num[1]//5
if num[1]%5!=0:
  ans+=1

print(ans)
'''
5
4+1
3+2
3+1+1
2+2+1
2+1+1+1
1+1+1+1+1
'''
