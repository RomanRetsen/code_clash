T = int(input())
for y in range(T):
    N, K, P = map(int, input().split())
    b_list = []
    for i in range(N):
        b_list.append([int(x) for x in input().split()][::-1])
    m_s = 0
    temp_max_number = 0
    temp_max_stack = None
    for p in range(P, 0, -1):
        for n in range(N):
            end_index = p if len(b_list[n]) >= p else len(b_list[n])
            if (sum(b_list[n][-end_index:])) > temp_max_number:
                temp_max_number = sum(b_list[n][-end_index:])
                temp_max_stack = n
        m_s += b_list[temp_max_stack].pop()
        temp_max_number = 0
        temp_max_stack = 0

    print(f"Case #{y+1}:", m_s)
