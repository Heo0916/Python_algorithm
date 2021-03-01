top_heights = [6, 9, 5, 7, 4]


# <- <- <- <- <-
def get_receiver_top_orders(heights):
    arr = [0] * len(heights) # [0, 0, 0, 0, 0]
    while heights:
        height = heights.pop()
        for idx in range(len(heights)-1, -1, -1):
            if heights[idx] > height:
                arr[len(heights)] = idx+1
                break
    return arr

print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
