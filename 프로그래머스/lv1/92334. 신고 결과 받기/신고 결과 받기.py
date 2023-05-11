import collections

def solution(id_list, reports, k):
    """
    id_list: 유저 리스트
    report: 신고 한 내역
    k: k 만큼 신고당하면 정지
    return value: id_list을 순회하면서 정지가 된 사람의 수의 List 반환
    """
    
    # 신고받음 사람 : [신고한 사람들]을 표현한 dict
    report_dict = collections.defaultdict(list)
    for report in reports:
        reporter, reported = report.split(" ")
        if reporter not in report_dict[reported]:
            report_dict[reported].append(reporter)
            
            
    # 
    result = []
    for id in id_list:
        cnt = 0
        for reported, reporter in report_dict.items():
            if len(reporter) >= k and id in reporter:
                cnt += 1
        result.append(cnt)
    
    return result
    
    