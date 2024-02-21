num = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

left = 0
right = num-1

min_sum = liquids[0]+liquids[num-1]
min_sum_left = 0
min_sum_right = num-1

flag = True
while left < right:
    temp_sum = liquids[left] + liquids[right]
    if temp_sum == 0: # 합이 0이 되는 조합을 찾았으면
        print(liquids[left], liquids[right]) # 출력하고
        flag = False
        break # 종료
    if abs(temp_sum) <= abs(min_sum): # 합이 0은 아니지만 지금까지 것들중에 제일 0에 가까우면
            min_sum_left = left
            min_sum_right = right # 일단 그 위치를 임시 저장
            min_sum = temp_sum

    # 포인터 이동
    if temp_sum < 0: # 합이 음수이면
            left += 1 # left를 한 칸 이동
    if temp_sum > 0: # 합이 양수이면
            right -= 1
if flag:
    print(liquids[min_sum_left], liquids[min_sum_right])
