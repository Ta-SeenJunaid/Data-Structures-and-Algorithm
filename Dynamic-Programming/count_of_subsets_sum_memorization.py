# https://www.youtube.com/watch?v=F7wqWbqYn9g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=9
# https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/

def count_sub_set_sum(a, t_sum, n):
    if t_sum==0:
        memo[n][t_sum] = 1
        return memo[n][t_sum]
    if n==0:
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
    a = [1, 5, 3, 7, 4]
    t_sum = 12
    n = len(a)
    memo = [[-1 for i in range(t_sum+1)] for j in range(n+1)]
    print(count_sub_set_sum(a, t_sum, n))

    a = [3, 34, 4, 12, 5, 2]
    t_sum = 30
    n = len(a)
    memo = [[-1 for i in range(t_sum+1)] for j in range(n+1)]
    print(count_sub_set_sum(a, t_sum, n))

    a = [1, 2, 3, 3]
    t_sum = 6
    n = len(a)
    memo = [[-1 for i in range(t_sum+1)] for j in range(n+1)]
    print(count_sub_set_sum(a, t_sum, n))

    a = [1, 1, 1, 1]
    t_sum = 1
    n = len(a)
    memo = [[-1 for i in range(t_sum+1)] for j in range(n+1)]
    print(count_sub_set_sum(a, t_sum, n))