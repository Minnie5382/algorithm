ex = input()
chunk = ex.split("-")
res = sum(list(map(int, chunk[0].split("+"))))
chunk = chunk[1:]

for c in chunk:
    res -= sum(list(map(int, c.split("+"))))
print(res)