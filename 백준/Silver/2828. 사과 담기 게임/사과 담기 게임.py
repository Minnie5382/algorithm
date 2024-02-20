screen_size, basket_size = map(int, input().split())
apple_number = int(input())
apples = [int(input()) for _ in range(apple_number)]

basket_start = 1 # 바구니의 시작점 (왼쪽점)
basket_end = basket_start + basket_size - 1 # 바구니의 끝점 (오른쪽점)

def move_to_left(gap):
    global basket_start, basket_end
    basket_start -= gap
    basket_end -= gap

def move_to_right(gap):
    global basket_start, basket_end
    basket_start += gap
    basket_end += gap

move = 0
for apple in apples:
    if basket_end < apple: # 현재 위치보다 사과가 오른쪽에 있으면
        gap = apple - basket_end
        move += gap
        move_to_right(gap)
    elif apple < basket_start: # 현재 위치보다 사과가 왼쪽에 있으면
        gap = basket_start - apple
        move += gap
        move_to_left(gap)
print(move)
