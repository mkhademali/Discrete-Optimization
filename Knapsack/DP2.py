def KnapSack(val, wt, n, W):
    dp = [0]*(W+1)
    X = [0] * n
    for i in range(n):
        for j in range(W, wt[i]-1, -1):
            if dp[j] > val[i] + dp[j-wt[i]]:
                X[i] = 1
            dp[j] = max(dp[j], val[i] + dp[j-wt[i]])
    return dp[W], X


# Driver program to test the cases
from asyncore import read
from itertools import count

def readfile(filename):
    with open(filename) as thefile:
        return thefile.read()


input_data = readfile('data/ks_4_0')
# parse the input
lines = input_data.split('\n')
firstLine = lines[0].split()
n = int(firstLine[0])
W = int(firstLine[1])

val = []
wt = []
for i in range(1, n+1):
    parts = lines[i].split()
    val.append(int(parts[0]))
    wt.append(int(parts[1]))
    

print(KnapSack(val, wt, n, W))
