def solution(numer1, denom1, numer2, denom2):
    for n in range(1,1000*1000):
        if n % denom1 == 0 and n % denom2 == 0:
            denom = n
            break
    a = denom / denom1
    b = denom / denom2
    numer = int(a * numer1 + b * numer2)
    for n in range(max(numer, denom),1,-1):
        if numer % n == 0 and denom % n == 0:
            numer = numer / n
            denom = denom / n
            break
    answer = [numer, denom]
    return answer