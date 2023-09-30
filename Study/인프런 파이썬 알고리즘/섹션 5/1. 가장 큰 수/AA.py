n, rcnt = map(int, input().split())
n = list(map(int, str(n)))
anslist=[]

for x in range(len(n)):

    while anslist and rcnt >0 and anslist[-1] < n[x]:
        anslist.pop()
        rcnt -=1

    anslist.append(n[x])

if rcnt != 0:
    anslist = anslist[:-rcnt]

res = "".join(map(str, anslist))
print(res)