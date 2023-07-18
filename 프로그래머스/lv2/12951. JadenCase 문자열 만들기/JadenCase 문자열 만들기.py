import string

def solution(s):
    
    answer = []
    
    for i in s.split(" "):
        answer_str = ""
        
        for index, j in enumerate(i):
            if index == 0 and j in string.ascii_letters:
                answer_str += j.upper()
            elif j in string.ascii_letters:
                answer_str += j.lower()
            else:
                answer_str += j
                
        answer.append(answer_str)
    
    return " ".join(answer)
        
    