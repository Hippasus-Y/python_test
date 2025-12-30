def solution(begin, target, words):
    import re
    connected = {}
    words = words + [begin]
    for word in words:
        listW = []
        for i, _ in enumerate(word):
            w_c = list(word)
            w_c[i] = '[a-z]'
            pattern = ''.join(w_c)
            matched = [wo for wo in words if re.match(pattern, wo)]
            listW.extend([wor for wor in matched if wor != word])
        connected[word] = listW
        
    print(connected)
    
    from collections import deque
    check = deque([begin])
    visited = set([begin])
    level = 0
    while check:
        b = len(check)
        for _ in range(b):
            c = check.popleft()
            if c == target:
                return level
            for n in connected[c]:
                if n not in visited:
                    visited.add(n)
                    check.append(n)
        level += 1
    return 0