import queue
maxLength = 100001

def prevent(next, prevent):
    if maxLength > next >= 0 and (visit[next] == 0 or visit[next] > visit[prevent] + 1):
        q.put(next)
        visit[next] = visit[prevent] + 1

if __name__ == "__main__":
    N, K = map(int, input().split())
    if not 100000 >= N >= 0 and 100000 >= K >= 0:
        exit(-1)
    q = queue.Queue()
    q.put(N)
    visit = [0] * maxLength

    while q:
        n = q.get()
        if n == K:
            print(visit[n])
            exit(0)
        prevent(n - 1, n)
        prevent(n + 1, n)
        prevent(n * 2, n)

