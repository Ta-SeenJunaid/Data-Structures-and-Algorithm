# https://www.youtube.com/watch?v=fJbIuhs24zQ&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=4


def knapsack(wt, val, w, n):
    if n==0 or w==0:
        return 0
    if memo[n][w] != -1:
        return memo[n][w]
    elif wt[n-1] > w:
        memo[n][w] = knapsack(wt, val, w, n-1)
        return memo[n][w]
    else:
        memo[n][w] = max(val[n-1] +
                   knapsack(wt, val, w-wt[n-1], n-1),
                   knapsack(wt, val, w, n-1))
        return memo[n][w]


if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    w = 50
    n = len(profit)
    memo = [[-1 for i in range(w+1)] for j in range(n+1)]
    print(knapsack(weight, profit, w, n))
