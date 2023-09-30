import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    jel = list(map(int, sys.stdin.readline().split()))
    gel = list(map(int, sys.stdin.readline().split()))
    trk = [sum(jel)]
    for r in range(1, k+1):
        jmax = max(jel)
        gmax = max(gel)
        jmin = min(jel)
        gmin = min(gel)
        if r%2==1:
            if min(jel) >= max(gel):
                trk.append(sum(jel))
                continue
            else:
                jel.append(gmax)
                gel.remove(gmax)
                gel.append(jmin)
                jel.remove(jmin)
        else:
            if  min(gel) >= max(jel):
                trk.append(sum(jel))
                continue
            else:
                jel.append(gmin)
                gel.remove(gmin)
                gel.append(jmax)
                jel.remove(jmax)
        trk.append(sum(jel))
        if r > 1:
            if trk[-3] == trk[-1]:
                if k%2==1 and r%2==1:
                    break
                elif k%2==0 and r%2==0:
                    break
    print(sum(jel))

# import sys
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n, m, k = map(int, sys.stdin.readline().split())
#     jel = list(map(int, sys.stdin.readline().split()))
#     gel = list(map(int, sys.stdin.readline().split()))
#     if k%2==1:
#         if min(jel) >= max(gel):
#             print(sum(jel))
#             continue
#         else:
#             print(sum(jel)-min(jel)+max(gel))
#             continue
#     else:
#         if min(gel) >= max(jel):
#             print(sum(jel))
#             continue
#         else:
#             print(sum(jel)+min(gel)-max(jel))
#             continue