N = int(input())

count = 1
num = 666
while count < N:
    num += 1
    if "666" in str(num):
        count += 1
print(num)
