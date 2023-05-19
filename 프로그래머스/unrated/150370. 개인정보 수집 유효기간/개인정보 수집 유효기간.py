from typing import List, Dict

def solution(today: str, terms: List[str], privacies: List[str]):
    
    # 모든 달은 28일 있다고 가정한다. 
    # 모든 날짜를 일별로 바꿔서 숫자 계산 
    
    def sum_days(day: str) -> int:
        year, month, day = day.split(".")
        return int(year) * 12 * 28 + int(month) * 28 + int(day)
    
    cases: Dict[str, int] = dict()
    
    for string in terms:
        case, term = string.split(" ")
        cases[case] = int(term) * 28
    
    today = sum_days(today)
    
    answer: List[int] = []
    
    for num, string in zip(range(1, len(privacies) + 1), privacies):
        day, terms = string.split(" ")
        
        if today >= sum_days(day) + cases[terms]:
            answer.append(num)
    
    return answer