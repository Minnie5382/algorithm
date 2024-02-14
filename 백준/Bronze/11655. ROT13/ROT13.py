sentence = input()
for s in sentence:
    if ord('a') <= ord(s) <= ord('z'): # 소문자이면
        print(chr((ord(s)-97+13)%26 +97), end="")
    elif ord('A') <= ord(s) <= ord('Z'): # 대문자이면
        print(chr((ord(s)-65+13)%26 +65), end="")
    else:
        print(s, end="")