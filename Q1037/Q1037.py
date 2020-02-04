
if __name__ == "__main__":
    N = int(input())
    N_list = list(map(int, input().split()))
    listSize = len(N_list)
    N_list.sort()
    maxValue = N_list[listSize-1]
    minValue = N_list[0]
    print(maxValue*minValue)
