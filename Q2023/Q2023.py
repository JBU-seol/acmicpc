# Recursive DFS

def isCorrect(tmp):
    if tmp < 2:
        return False
    for i in range(2, tmp):
        if i*i > tmp:
            break
        if tmp % i == 0:
            return False
    return True

def recursive(do, n):
    if n == 0:
        print(do)
    else:
        for i in range(1, 10, 2):
            tmp = do * 10 + i
            if isCorrect(tmp):
                recursive(tmp, n - 1)

if __name__ == "__main__":
    N = int(input())
    if not 8 >= N >= 1:
        exit(-1)

    canDo = [2, 3, 5, 7]
    for do in canDo:
        recursive(do, N-1)



