# https://www.youtube.com/watch?v=ntCGbPMeqgg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=5


def knapsack(wt, val, w, n):
    tb = [[0 for x in range(w+1)] for y in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                tb[i][j] = 0
            elif wt[i-1] > w:
                tb[i][j] = tb[i-1][j]
            else:
                tb[i][j] = max(val[i-1] + tb[i-1][w-wt[i-1]],tb[i-1][j])
    return tb[n][w]

if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    w = 50
    n = len(profit)
    print(knapsack(weight, profit, w, n))
