def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])    # 비용이 적은 순으로 sort
    connect = set([costs[0][0]])    # 첫번째로 비용이 가장 적은 것이 왔으니 일단 첫번째 섬은 무조건 연결
    
    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(connect) != n:    # connect에 모든 섬이 다 차면(연결되면) while문 빠져나감
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            elif cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])    # set이라서 중복안되게 연결됨(update함수 사용)
                answer += cost[2]
                break    # 꼭 필요 -> while문으로 다시 돌아가서 모든 섬이 찼는지 확인 후 다시 for문 
                
    return answer