from collections import deque

def solution(people, limit):
    """
    1. people을 내림차순으로 정리한 후 앞 요소와 맨 뒷 요소를 더한 값이 limit 넘는지 체크
    2. limit 넘으면 앞 요소만 제거한 후 answer 값을 + 1
    3. limit 을 넘지 않으면 앞, 뒤 요소 모두 제거한 후 answer 값을 + 1
    """
    answer = 0
    people_copy = deque(sorted(people.copy(), key=lambda x: -x))

    while people_copy:
        if len(people_copy) == 1:
            answer += 1
            people_copy.popleft()
        else:
            if people_copy[0] + people_copy[-1] <= limit:
                people_copy.popleft()
                people_copy.pop()
                answer += 1
            else:
                people_copy.popleft()
                answer += 1

    
    return answer