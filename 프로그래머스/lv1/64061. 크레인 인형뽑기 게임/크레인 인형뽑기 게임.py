def solution(board, moves):
    
    bucket = []
    answer = 0
    
    for catch in moves:
        for row in board:
            column = catch - 1
            if row[column] != 0:
                if len(bucket) != 0 and bucket[-1] == row[column]:
                    bucket.pop()
                    row[column] = 0
                    answer += 1
                else:
                    bucket.append(row[column])
                    row[column] = 0
                break
    
    return answer * 2