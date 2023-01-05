import sys

N = int(sys.stdin.readline())
dp =[[0,1,1,1,1,1,1,1,1,1], [1,1,2,2,2,2,2,2,2,1]]


for i in range(2, N):
    cur_res = [0,0,0,0,0,0,0,0,0,0]

    for j in range(10):
        if j == 0:
            cur_res[j] = dp[i-1][j+1]

        elif j == 9:
            cur_res[j] = dp[i-1][j-1]

        else:
            cur_res[j] = dp[i-1][j-1] + dp[i-1][j+1]
    
    dp.append(cur_res)
    
print(dp)
print(sum(dp[N-1])%1000000000)