def solution(myString, pat):
    
    count = 0
    
    for i in range(len(myString)):
        if myString[i: i + len(pat)] == pat:
            count += 1
            
    return count