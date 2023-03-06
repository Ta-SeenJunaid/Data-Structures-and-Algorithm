# https://www.youtube.com/watch?v=-GtpxG6l_Mc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=10&t=419s

def minimum_sub_set_sum_difference(a, t_sum, n):
    table = [[False for i in range(t_sum+1)] for j in range(n+1)]
    for i in range(n+1):
        table[i][0] = True
    for i in range(1, n+1):
        for j in range(1, t_sum+1):
            if a[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j-a[i-1]] or table[i-1][j]
    min_def = float('inf')
    for i in range(0, (t_sum)//2+1):
        if table[n][i]:
            min_def = min(min_def, t_sum-2*i)
    return min_def


if __name__ == '__main__':
    a = [1, 2, 7]
    t_sum = sum(a)
    n = len(a)
    print(minimum_sub_set_sum_difference(a, t_sum, n))

    a = [1, 6, 11, 5]
    t_sum = sum(a)
    n = len(a)
    print(minimum_sub_set_sum_difference(a, t_sum, n))

