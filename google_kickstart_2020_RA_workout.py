
def solve():
    N, K = [int(x) for x in input().split()]
    exes_minutes = [int(x) for x in input().split()]
    for k in range(K+1):
        most_diff_number = 0
        most_diff_level = -1
        for n in range(1, N+k):
            diff = exes_minutes[n] - exes_minutes[n-1]
            if diff > most_diff_number:
                most_diff_number = diff
                most_diff_level = n
        exes_minutes.insert(most_diff_level, exes_minutes[most_diff_level-1] + most_diff_number//2)
    else:
        return most_diff_number

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        print(f'Case #{t+1}', solve())