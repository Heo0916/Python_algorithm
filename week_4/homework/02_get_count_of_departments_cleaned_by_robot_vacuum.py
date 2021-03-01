current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
#1 . 현재 위치를 청소한다.
#bfs = visited = []
# 0 은 청소하지 않은 장소
# 1 은 청소하지 못하는 장소
# 2 는 청소한 장소

# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색을 진행한다.

#북쪽 r, c -1 0
#동쪽      0, 1
#남쪽      1, 0
#서쪽      0, -1
#     북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 북 0, 동 1 남 2 서 3
# 북 왼 회전 -> 서 (0 -> 3)
# 동 왼 회전 -> 북 (1- -> 0)
# 남 왼 회전 -> 동 (2 -> 1)
# 서 왼 회전 -> 남 (3 -> 2)

# 북 뒤 돌기 -> 남 0 -> 2
# 동 뒤 돌기 -> 서 1 -> 3
# 남 뒤 돌기 -> 북 2 -> 0
# 서 뒤 돌기 -> 동 3 -> 1
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4

def get_d_index_when_go_back(d):
    return (d + 2) % 4
# bfs로 구현
#1. 현재 위치 청소
# bfs 를 구현 할때 visited = [1 2, 3]
# 0은 청소하지 않은 장소
# 1은 청소하지 못하는 장소
# 2는 청소한 장소.

# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색 진행

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)  #행
    m = len(room_map[0]) #열
    count_of_departments_cleaned = 1
    room_map[r][c] = 2
    queue = list([[r, c, d]])

    while queue:
        r, c, d = queue.pop(0)
        temp_d = d

        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break
            # c. 네 방향 모두 청소가 되어 있거나, 벽인 경우
            # 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로
            elif i == 3:
                new_r, new_c = r + dr[get_d_index_when_go_back(temp_d)], c + dc[get_d_index_when_go_back(temp_d)]
                queue.append([new_r, new_c, temp_d])
            #d. 네 방향 모두 청소가 이미 되어있거나 벽.
            # 뒤쪽 방향이 벽이라 후진도 못하는 경우 작동 멈춤
                if current_room_map[new_r][new_c] == 1:
                    return count_of_departments_cleaned
    return

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))