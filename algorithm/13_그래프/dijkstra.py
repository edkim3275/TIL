def dijstra():
    dist = [987654321] * (V+1)
    visited = [0] * (V+1)

    dist[0] = 0

    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        for i in range(V+1):
            if not visited[i] and min_value > dist[i]:
                min_value = dist[i]
                min_idx = i
        visited[min_idx] = 1
        # 갱신할 것들 갱신
        for i in range(V+1):
            if not visited[i] and dist[i] > adj[min_idx][i] + dist[min_idx]:
                dist[i] = adj[min_idx][i] + dist[min_idx]

    return sum(dist)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[987654321]*(V+1) for _ in range(V+1)]

    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = w

