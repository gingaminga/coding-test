def solution(board, moves):
    answer = 0
    
    print("원본")
    for row in board:
        for item in row:
            print(item,end=" ")
        print()
    
    columns = []
    for i in range(len(board)):
        column = [row[i] for row in board if row[i] != 0]
        columns.append(column)
    
    picker = []
    for i in range(len(moves)) :
        if columns[moves[i] - 1]:
            selectedItem = columns[moves[i] - 1][0]
            
            if len(picker) < 1:
                picker.append(columns[moves[i] - 1][0])
            elif picker[len(picker) - 1] == selectedItem:
                picker.pop(len(picker) - 1)
                answer += 2
            else:
                picker.append(columns[moves[i] - 1][0])
        
            columns[moves[i] - 1].pop(0)
                
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]) # 4

# https://programmers.co.kr/learn/courses/30/lessons/64061