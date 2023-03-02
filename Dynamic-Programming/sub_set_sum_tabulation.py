# https://www.youtube.com/watch?v=_gPcYovP7wc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=7
# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

def is_sub_set_sum(a, t_sum, n):
    table = [[False for i in range(t_sum+1)] for j in range(n+1)]
    for i in range(n+1):
        table[i][0] = True
    for i in range(1, n+1):
        for j in range(1, t_sum+1):
            if a[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] or table[i-1][j-a[i-1]]
    return table[n][t_sum]


if __name__ == '__main__':
    a = [1, 5, 3, 7, 4]
    t_sum = 12
    n = len(a)
    print(is_sub_set_sum(a, t_sum, n))

    a = [3, 34, 4, 12, 5, 2]
    t_sum = 30
    n = len(a)
    print(is_sub_set_sum(a, t_sum, n))

