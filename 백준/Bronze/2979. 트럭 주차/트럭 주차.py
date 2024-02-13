from collections import Counter

A, B, C = map(int, input().split())
parking_lot = [0 for _ in range(100)]
parking_times = []
for _ in range(3):
    parking_times.append(list(map(int, input().split())))

for start, end in parking_times:
    for i in range(start, end):
        parking_lot[i] += 1

cntr = Counter(parking_lot)
print(cntr[1]*A + cntr[2]*B*2 + cntr[3]*C*3)