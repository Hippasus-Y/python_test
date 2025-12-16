def solution(n):
    for m in range(1,6*n+1):
        if m % 6 == 0 and m % n ==0:
            answer = m // 6
            break
    return answer