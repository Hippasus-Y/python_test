def solution(babbling):
    a = "aya"
    b = "ye"
    c = "woo"
    d = "ma"
    answer = 0
    from itertools import permutations
    listC = [''.join(p) for r in range(1, 5) for p in permutations([a, b, c, d], r)]
    for bab in babbling:
        if bab in listC:
            answer += 1
    return answer