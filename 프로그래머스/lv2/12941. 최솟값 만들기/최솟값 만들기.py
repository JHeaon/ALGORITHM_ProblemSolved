def solution(A,B) -> int:
    """
    두 배열의 각각의 곱이 최소가 되기 위해서는 A배열은 내림차순으로 정렬 B배열은 오름차순으로 정렬 후
    각 배열을 순회하면서 곱한 값을 더한 것이 최솟값이 될 수 있다. 
    """
    
    A = sorted(A)
    B = sorted(B, key=lambda x: -x)
    answer: int = 0
    
    for a, b in zip(A, B):
        answer += a * b
    
    return answer