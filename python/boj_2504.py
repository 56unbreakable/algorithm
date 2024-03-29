from collections import deque

string = input()


def solution(string):
    stack = deque()
    for s in string:
        if s == "(" or s == "[":
            stack.append(s)
            continue
        
        tmp = 0
        if s == ")" or s == "]":
            while True:
                if stack:
                    b = stack.pop()
                else:
                    return 0

                if b == "(" and s == ")":
                    if tmp == 0:
                        stack.append(2)
                    else:
                        stack.append(tmp * 2)
                    break
                
                elif b == "[" and s == "]":
                    if tmp == 0:
                        stack.append(3)
                    else:
                        stack.append(tmp * 3)
                    break
            
                elif isinstance(b,int):
                    tmp += b

                else:
                    return 0
    answer = 0
    while stack:
        a = stack.pop()
        if isinstance(a,int):
            answer += a
        else:
            return 0

    return answer

print(solution(string))