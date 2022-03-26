import heapq

def solution(jobs):
    answer = 0
    start, now = -1, 0    # start=이전 작업을 마무리한 시각, now=현재 시각
    i = 0    # 모든 jobs를 확인하기 위해서 존재
    heap = []
    
    while i < len(jobs):
        for job in jobs:  # 작업들 중 now시각 안에 작업할 수 있는 것들을 heap에 저장
            if start < job[0] <= now:  # 내가 작업을 하는 도중에 요청이 들어왔을 수 있으니까 start < <=now
                heapq.heappush(heap, [job[1], job[0]])  # (작업시간 기준)최소힙
                
        if len(heap) > 0:  # heap이 만들어 졌다면(존재한다면)
            cur = heapq.heappop(heap)    # 가장 짧은 소요시간 작업이 나오게 됨(이유:최소힙)
            start = now
            now += cur[0]
            answer += now-cur[1]  # 요청부터 종료까지 소요시간
            i += 1
        else:  # heap이 만들어지지 않았다면
            now += 1
            # i는 왜 안 더하지?
    return answer / len(jobs)