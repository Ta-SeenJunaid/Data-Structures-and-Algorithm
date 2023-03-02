# https://www.youtube.com/watch?v=UmMh7xp07kY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=9
# https://www.geeksforgeeks.org/partition-problem-dp-18/

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
    a = [1, 5, 11, 5]
    a_sum = sum(a)
    if a_sum%2 != 0:
        print("Not possible")
    else:
        n = len(a)
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
        if is_sub_set_sum(a, a_sum//2, n):
            print("Possible")
        else:
            print("Not possible")