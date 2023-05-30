from typing import List

def solution(wallpaper: List[List[str]]) -> List[int]:
    
    min: List[int, int] = [len(wallpaper) ,len(wallpaper[0])]
    max: List[int, int] = [0, 0]
    
    for x, elements in enumerate(wallpaper):
        for y, element in enumerate(elements):
            if element == "#":
                if x <= min[0]:
                    min[0] = x
                if y <= min[1]:
                    min[1] = y
                if x >= max[0]:
                    max[0] = x
                if y >= max[1]:
                    max[1] = y
        
    answer: List[int] = min + [i + 1 for i in max]
    return answer