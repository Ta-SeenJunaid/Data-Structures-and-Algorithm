# https://www.youtube.com/watch?v=_gPcYovP7wc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=7
# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

def is_sub_set_sum(a, t_sum, n):
    if t_sum==0:
        return True
    if n==0:
        return False
    if memo[n][t_sum] != -1:
        return memo[n][t_sum]

    if a[n-1] > t_sum:
        memo[n][t_sum] = is_sub_set_sum(a, t_sum, n-1)
        return memo[n][t_sum]
    else:
        memo[n][t_sum] = is_sub_set_sum(a, t_sum-a[n-1], n-1) \
                         or is_sub_set_sum(a, t_sum, n-1)
        return memo[n][t_sum]

if __name__ == '__main__':
    a = [1, 5, 3, 7, 4]
    t_sum = 12
    n = len(a)
    memo = [[-1 for i in range(t_sum+1)] for j in range(n+1)]
    print(is_sub_set_sum(a, t_sum, n))

    a = [3, 34, 4, 12, 5, 2]
    t_sum = 30
    n = len(a)
    memo = [[-1 for i in range(t_sum+1)] for j in range(n+1)]
    print(is_sub_set_sum(a, t_sum, n))

