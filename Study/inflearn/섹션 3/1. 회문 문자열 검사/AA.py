n = int(input())

for x in range(n):
    txt = str(input())
    txt = txt.lower()

    if txt[::-1] == txt:
        print(f"#{x+1} YES")
    
    else:
        print(f"#{x+1} NO")
