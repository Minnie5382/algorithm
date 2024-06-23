N = int(input())
points = []
for _ in range(N):
    p = list(map(int, input().split()))
    points.append(p)

x_points = set()
y_points = set()
for point in points:
    x_points.add(point[0])
    y_points.add(point[1])

for member in range(1, N+1): # member = 모이는 사람 수
    total_distance = []
    for x in x_points:
        for y in y_points: # (x, y) = 모이는 지점
        # (x, y)에서 member 명수만큼 모이는 경우의 최단거리를 계산해서 최소값을 출력

            distance = [] # (x, y)~각 점 사이의 거리
            for xi, yi in points:
                distance.append(abs(x-xi)+abs(y-yi))
            distance.sort()
            total_distance.append(sum(distance[:member]))
    print(min(total_distance), end=" ")