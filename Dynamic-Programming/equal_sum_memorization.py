# https://www.youtube.com/watch?v=UmMh7xp07kY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=9
# https://www.geeksforgeeks.org/partition-problem-dp-18/

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
    a = [1, 5, 11, 5]
    a_sum = sum(a)
    if a_sum%2 != 0:
        print("Not possible")
    else:
        n = len(a)
        memo = [[-1 for i in range(a_sum//2+1)] for j in range(n+1)]
        if is_sub_set_sum(a, a_sum//2, n):
            print("Possible")
        else:
            print("Not possible")

    a = [1, 5, 3]
    a_sum = sum(a)
    if a_sum%2 != 0:
        print("Not possible")
    else:
        n = len(a)
        memo = [[-1 for i in range(a_sum//2 + 1)] for j in range(n + 1)]
        if is_sub_set_sum(a, a_sum//2, n):
            print("Possible")
        else:
            print("Not possible")
