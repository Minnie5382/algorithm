str = input()

prev = '-1'
trun_str = ""
for i in range(len(str)):
  if str[i] != prev:
    trun_str += str[i]
    prev = str[i]

answer = trun_str.count('01') if trun_str.startswith('0') else trun_str.count('10')

print(answer)
