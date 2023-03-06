# https://www.youtube.com/watch?v=ot_XBHyqpFc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=13

def count_sub_set_sum(a, t_sum, n):
    if t_sum == 0:
        memo[n][t_sum] = 1
        return memo[n][t_sum]
    if n == 0:
        memo[n][t_sum] = 0
        return memo[n][t_sum]
    if memo[n][t_sum] != -1:
        return memo[n][t_sum]
    if a[n-1] > t_sum:
        memo[n][t_sum] = count_sub_set_sum(a, t_sum, n-1)
        return memo[n][t_sum]
    else:
        memo[n][t_sum] = count_sub_set_sum(a, t_sum-a[n-1], n-1) \
                         + count_sub_set_sum(a, t_sum, n-1)
        return memo[n][t_sum]


if __name__ == '__main__':
    a = [1, 1, 2, 3]
    diff = 2
    t_sum = (sum(a)+diff)//2
    n = len(a)
    memo = [[-1 for i in range(n+1)] for j in range(t_sum+1)]
    print(count_sub_set_sum(a, t_sum, n))