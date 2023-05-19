from typing import List

def solution(ingredient: List[int]):
    
    case: List[int] = []
    count: int = 0
    
    for i in ingredient:
        case.append(i)
        if case[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                case.pop()
            count += 1
            
    return count