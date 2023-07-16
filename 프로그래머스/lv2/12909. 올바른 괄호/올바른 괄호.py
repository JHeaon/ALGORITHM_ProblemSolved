from collections import deque 

def solution(s) -> bool:
    """
    괄호 문제는 stack을 이용하여 처리하면 쉽게 처리 할 수 있다. 
    """
    
    stack = deque()
    
    for element in s:
        if element == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    else:
        return True
    
        
            
    
    