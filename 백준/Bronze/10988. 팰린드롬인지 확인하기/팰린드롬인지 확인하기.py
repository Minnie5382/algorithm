word = input()
res = 1
for i in range(len(word)//2):
    if word[i] != word[i*(-1)-1]:
        res = 0
print(res)