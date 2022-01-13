def get_prefix(A):
    temp = [0]*(len(A))
    for i, val in enumerate(A):
        temp[i] = val
        if i > 0:
            temp[i] += temp[i-1]
    return temp

def bs(A,left,right, key, offset = 0):
    ans = -1
    while left <= right:
        mid = left + (right-left)//2
        if A[mid]-offset <= key:
            ans = mid
            left = mid+1
        else:
            right = mid-1
    return ans

def bs_right(A,left,right, key, offset = 0):
    ans = -1
    while left <= right:
        mid = left + (right-left)//2
        if A[mid]-offset >= key:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    return ans

def solve (N, Q, A, query):
    # Write your code here
    target = sum(A)//2
    s = sum(A)
    ans = []
    has = {}
    A += A
    prefix = get_prefix(A)
    for path, times in query:
        times = times%N
            
        if path == 2:
            offset = prefix[times-1] if times>0 else 0
            start = times
            end = N+times-1
            
        else:
            offset = prefix[N-times-1]
            start = N-times
            end = 2*N - times-1
        if (start, end) in has:
            ans.append(has[(start, end)])
        else:
            index = bs(prefix,start, end, target, offset)
            index2 = bs_right(prefix, start,end, target, offset)
            has[(start, end)] = min(abs(s - 2*(prefix[index]-offset)),abs(s - 2*(prefix[index2]-offset)))
            ans.append(has[(start, end)])
    return ans

T = int(input())
for _ in range(T):
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    query = [list(map(int, input().split())) for i in range(Q)]

    out_ = solve(N, Q, A, query)
    print (' '.join(map(str, out_)))