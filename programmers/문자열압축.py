def solution(s):
    answer = 1000
    if len(s) == 1:
        return 1
    for n in range(1, len(s)//2+1):
        res = ''
        cnt = 1
        tmp = s[:n]
        for i in range(n, len(s), n):
            if tmp == s[i:i+n]:
                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt)+tmp
                    
                tmp = s[i:i+n]
                cnt = 1
        if cnt != 1:
            res += str(cnt)+tmp
        else:
            res += tmp
        answer = min(answer, len(res))
        
    return answer