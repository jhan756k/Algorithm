import sys
n, r, c = map(int, sys.stdin.readline().split())
t = 2**n
def div(r, c, n, val):
    d = n//2
    if n==1:
        print(val)
        exit()
    if n!=2:
        tx = r//d
        ty = c//d
    else:
        tx = r
        ty = c
    if tx==0 and ty==0:
        div(r, c, d, val)
    elif tx==0 and ty>0:
        div(r, c-d, d, val + ((d)**2))
    elif tx>0 and ty==0:
        div(r-d, c, d, val + 2*((d)**2))
    elif tx >0 and ty>0:
        div(r-d, c-d, d, val + 3*((d)**2))
div(r, c, t, 0)

# cnt = 0
# def div(x, y, n):
#     global cnt
#     if n!= 1:
#         div(x,y,n//2)
#         div(x,y+n//2,n//2)
#         div(x+n//2,y,n//2)
#         div(x+n//2,y+n//2,n//2)
#         return
#     else:
#         if x == r and y == c:
#             print(cnt)
#             exit()
#         else:
#             cnt+=1
# div(0, 0, 2**n)