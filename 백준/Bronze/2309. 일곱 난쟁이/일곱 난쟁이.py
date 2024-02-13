heights = [int(input()) for _ in range(9)]
heights.sort()
for i in range(len(heights)):
    for j in range(i+1, len(heights)):
        heights_copy = heights[:i] + heights[i+1:j] + heights[j+1:]
        if sum(heights_copy) == 100:
            for h in heights_copy:
                print(h)
            break
    if sum(heights_copy) == 100:
        break