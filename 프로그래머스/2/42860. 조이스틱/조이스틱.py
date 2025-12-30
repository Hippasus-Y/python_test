def solution(name):
    listA = list('BCDEFGHIJKLMN')
    listB = list('ZYXWVUTSRQPO')
    cc = 0
    for c in name:
        if c == 'A':
            continue
        elif c in listA:
            cc += listA.index(c)+1
        elif c in listB:
            cc += listB.index(c)+1
    listN = list(name[1:])
    listM = list(reversed(listN))
    
    cpn = 0; cpm = 0
    c_pn = 0; c_pm = 0
    for n in listN:
        c_pn += 1
        if n != 'A':
            cpn += c_pn
            c_pn = 0
    for m in listM:
        c_pm += 1
        if m != 'A':
            cpm += c_pm
            c_pm = 0
            
    maxA = ''
    for i in range(1,21):
        if 'A'*i in name:
            maxA = 'A'*i
    if maxA:
        subi = name.index(maxA)
        if subi == 0:
            fi = 0
        else:
            fi = subi-1
        bi = len(name) - (subi + len(maxA))
        ftob = fi*2 + bi
        btof = bi*2 + fi
        cp = min(cpn, cpm, ftob, btof)
    else:
        cp = min(cpn, cpm)
    print(cc,cp)
    answer = cc + cp
    return answer