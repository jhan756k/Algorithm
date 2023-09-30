t = str(input())
ans = ""

for letter in t:
    if letter.isdecimal():
        ans+=letter
ans = int(ans)

cnt = 0

for x in range(1, ans+1):
    if ans%x == 0:
        cnt +=1

print(ans)
print(cnt)
