def solution(n):
    if n == 0 or n == 1:
        return 0
    sum = 0
    for i in range(2,n+1,2):
        sum += i
    return sum