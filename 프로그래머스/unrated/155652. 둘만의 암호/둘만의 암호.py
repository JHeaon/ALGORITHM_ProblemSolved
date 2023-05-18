import string

def solution(s, skip, index):
    case = list(string.ascii_lowercase)
    
    # 순회하면서 skip 요소 제거
    for element in skip:
        case.remove(element)
    
    # case 길이를 늘려서 만약 index가 초과 됬을 때 다음 요소를 바로 찾을 수 있게 설정
    # 해당 방법을 할 수 있었던 근거 : 제한 사항에서 INDEX 길이가 길지 않음.
    case *= 3
    
    answer = ""
    
    for element in s:
        answer += case[case.index(element) + index]
    
    return answer