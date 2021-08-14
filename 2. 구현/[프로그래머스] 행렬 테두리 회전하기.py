def solution(rows, columns, queries):
    # 초기 사각형 만들기
    grid = []
    num = 0
    
    for _ in range(rows):
        t = []
        for _ in range(columns):
            num += 1
            t.append(num)
        grid.append(t)
    
    answer = []
    
    # 쿼리받는 반복문
    for q in queries:
        # ogrid = copy.deepcopy(grid) # 전단계의 grid를 저장해둔다
        x1, y1, x2, y2 = q 
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1 # 위치를 변경할 사각형의 꼭짓점(인덱스 위해 -1)
        w = y2-y1 # width
        h = x2-x1 # heigth
        
        loop = [range(w), range(h)]*2
        
        x, y = x1, y1
        result = int(1e9)
        
        oval = grid[x][y] # 전단계의 orginal value
        for i in range(4): # 우 하 좌 상
            for ii in loop[i%4]: 
                if  oval < result:
                    result = oval
                if i%4 == 0:
                    y += 1
                    
                elif i%4 == 1:
                    former_x = x
                    x += 1
                    
                elif i%4 == 2:
                    former_y = y
                    y -= 1
                      
                elif i%4 == 3:
                    former_x = x
                    x -= 1
                    
                ooval = grid[x][y] # 지금단계의 original_value
                grid[x][y] = oval # 전단계의 original_value
                oval = ooval 
                
        answer.append(result)
    return answer