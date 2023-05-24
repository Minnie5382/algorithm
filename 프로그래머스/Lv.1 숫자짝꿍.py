def solution(X, Y):
    X_plate = [0 for i in range(10)]
    Y_plate = [0 for i in range(10)]
    inter = [0 for i in range(10)]
    answer = ""
    for n in X:
        for e in range(10):
            if n == str(e):
                X_plate[e] += 1
    for n in Y:
        for e in range(10):
            if n == str(e):
                Y_plate[e] += 1
    
    for i in range(10) :
        inter[i] = min(X_plate[i], Y_plate[i])

    for j in range(9, -1, -1):
        if inter[j] != 0:
            answer += str(j)*int(inter[j])
            
    if answer == "":
        return "-1"
    elif set(answer) == {'0'}:
        return "0"
    
    return answer
