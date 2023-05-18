from collections import defaultdict

def solution(keymaps, targets):
    
    # 최소 숫자로 찾을 수 있는 dict형 만듬
    case = defaultdict(int)
    for keymap in keymaps:
        for count, alphabet in enumerate(keymap):
            if case[alphabet] == 0:
                case[alphabet] = count + 1
            elif case[alphabet] > count:
                case[alphabet] = count + 1
 

    answer = []
    for target in targets:        
        count = 0
        for alphabet in target:
            if case[alphabet] == 0:
                count = 0
                break
            else:
                count += case[alphabet]
        
        if count == 0:
            answer.append(-1)
        else:
            answer.append(count)
        
    
    return answer