# https://www.youtube.com/watch?v=ot_XBHyqpFc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=13

def count_sub_set_sum(a, t_sum, n):
    table = [[0 for i in range(t_sum+1)] for j in range(n+1)]
    for i in range(n+1):
        table[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, t_sum+1):
            if a[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j-a[i-1]] + table[i-1][j]
    return table[n][t_sum]


if __name__ == '__main__':
    a = [1, 1, 2, 3]
    diff = 2
    t_sum = (sum(a)+diff)//2
    n = len(a)
    print(count_sub_set_sum(a, t_sum, n))