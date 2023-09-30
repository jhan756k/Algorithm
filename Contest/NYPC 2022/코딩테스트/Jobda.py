# import requests, random

# url = "https://badada.gibal.net/result/"
# cnt = 0

# while True:
#     data = {"answer":[1,2,3,4,random.randint(12, 15),6,7,random.randint(12,15),9,10,11,random.randint(12, 15)]}
#     res = requests.post(url, json=data)
#     cnt += 1
#     if res.status_code == 500:
#         exit()
#     print(cnt)

def Pcal(a, b):
    tm1 = a
    tm2 = b
    while True:
        if (tm1%2==0 and tm1!=0) and (tm2%2==0 and tm2!=0):
            tm1>>=1
            tm2>>=2  
        else:
            if (tm1%2==1 or tm1==0) and not (tm2%2==1 or tm2==0):
                return b
            else:
                return a

def solution(N, M):
    idlist = [x for x in range(1, N+1)]
    winlist = []
    ans = []
    while len(idlist) > 1:
        
        for x in range(0, len(idlist), 2):
            if idlist[x] == M:
                ans.append(idlist[x+1])
                winlist.append(M)
            elif idlist[x+1] == M:
                ans.append(idlist[x])
                winlist.append(M)
            else:
                winlist.append(Pcal(idlist[x], idlist[x+1]))
        idlist = [x for x in winlist]
        winlist = []
    return ans

print(solution(16, 10))


# def group(n, arr):
#     ans = []
#     for i in range(0, n, 2):
#         ans.append(arr[i:i+2])
#     return ans 

# def solution(N, M):
#     idlist = [x for x in range(1, N+1)]
#     ans = []

#     while len(idlist) != 1:
#         fight = group(len(idlist), idlist)
#         idlist = []

#         for f in fight:
#             if f[0] == M:
#                 ans.append(f[1])
#                 idlist.append(M)
#             elif f[1] == M:
#                 ans.append(f[0])
#                 idlist.append(M)
#             else:
#                 m1, m2 = 1, 1
#                 tm1, tm2 = f[0], f[1]

#                 while True:
#                     if (tm1%2==0 and tm1!=0) and (tm2%2==0 and tm2!=0):
#                         tm1/=2
#                         tm2/=2
#                     else:
#                         if (tm1%2==1 or tm1==0) and not (tm2%2==1 or tm2==0):
#                             idlist.append(f[1])
#                             break
#                         else:
#                             idlist.append(f[0])
#                             break
#     return ans