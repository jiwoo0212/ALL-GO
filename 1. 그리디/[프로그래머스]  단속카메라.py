def solution(routes):
    routes.sort(key=lambda x: x[1]) # 나오는 시간대로 오름차순 정렬
    camera = []
    camera.append(routes[0][1]) # 카메라 설치 시간대
    done = [False for _ in range(len(routes))] # 카메라 설치가 되었는지
    
    for i in range(len(routes)):
        for c in camera:
            if routes[i][0] <= c <= routes[i][1]: # 설치된 카메라가 구간안에 있다면
                done[i] = True
                break
        # 설치된 모든 카메라가 해당 구간안에 없다면 해당구간의 마지막에 카메라 설치        
        if done[i] == False: 
            camera.append(routes[i][1])
            
    return len(camera)