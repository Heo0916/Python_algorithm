seat_count = 9
vip_seat_array = [4, 7]

#[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
1 2 3
5 6
8 9

좌석 [1, 2]
[1, 2] [2, 1] -> 2

좌석 [1, 2, 3]
[1, 2, 3] [2, 1, 3] [1, 3, 2] -> 3 

좌석 [1, 2, 3, 4] 
[1, 2, 3, 4] [1, 2, 4, 3] [1, 3, 2, 4] [2, 1, 3, 4] [2, 1, 4, 3] -> 5
좌석 [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5] [1, 2, 3, 5, 4],,,,, -> 8

좌석(2) = 2
좌석(3) = 3

F(N) = N 명의 사람들을 좌석에 배치하는 방법
     = N-1 명의 사람들을 좌석에 배치한느 방법 + N-2 명의 사람들을 좌석에 배치하는 방법
     = F(N-1) + F(N-2)
'''
memo = {
    1: 1,
    2: 2
}

# f(100)->f(99) -> f(98) ...Top down 방식

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo  # 기록하는 부분

    return nth_fibo






def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat-1

        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways

    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))