p = list(str(input()).split())
blacklist = list(map(str.lower, str(input()).split()))
r = list(str(input()).split())
words, before, after = [], [], []
[words.append(i) for i in p if i.lower() not in blacklist]
words = sorted(words, key=str.casefold)

def punc(word):
    if word[-1] in '.?!,;:': return True
    else: return False

def find_context(ind, bi, ai):
    btemp, atemp = [], []
    for i in range(ind-1, bi-1, -1):
        if punc(p[i]) or (p[i].lower() in blacklist): break
        else: btemp.append(p[i])
    btemp.reverse()
    before.append(' '.join(btemp))

    if punc(p[ind]): 
        after.append("")
        return
    
    for i in range(ind+1, ai+1):
        if (p[i].lower() in blacklist): break
        elif punc(p[i]):
            atemp.append(p[i][:-1])
            break
        else: atemp.append(p[i])
    if len(atemp) == 0: after.append("")
    else: after.append(' '.join(atemp))

modp = list()
[modp.append(x) for x in p]

for w in words:     
    for i in range(len(p)):
        if modp[i] == w: 
            modp[i] = None
            bi = i-3 
            ai = i+3
            if i < 3: bi = 0
            if i >= len(p)-3: ai = len(p)-1

            find_context(i, bi, ai)
            break
                
finalword = list()
for i in range(len(words)):
    if punc(words[i]): finalword.append(words[i][:-1])
    else: finalword.append(words[i])

beforemax = max([len(x) for x in before])
aftermax = max([len(x) for x in after])
wordmax = max([len(x) for x in finalword])

dashnum = []

for i in range(int(r[0])-1, int(r[1])):
    temp = beforemax - len(before[i])
    temp += aftermax - len(after[i])
    temp += wordmax - len(finalword[i])
    dashnum.append(temp)

ansind = dashnum.index(min(dashnum)) + int(r[0])-1

anstr = before[ansind] + ('-'*(beforemax - len(before[ansind]))) + " "
anstr += "<" + finalword[ansind] + ('-'*(wordmax - len(finalword[ansind]))) + "> "
anstr += after[ansind] + ('-'*(aftermax - len(after[ansind])))

print(anstr)