# https://www.youtube.com/watch?v=SZqAQLjDsag&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=14
# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
from typing import Optional, List


def rod_cutting(length:Optional[List], price:Optional[List], n:int):
    table = [[0 for i in range(n+1)] for j in range(len(length)+1)]
    for i in range(1, len(length)+1):
        for j in range(1, n+1):
            if length[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(price[i-1]+table[i][j-length[i-1]], table[i-1][j])
    return table[len(length)][n]


if __name__ == '__main__':
    length = [1,   2,   3,   4,   5,   6,   7,   8]
    price = [1,   5,   8,   9,  10,  17,  17,  20]
    n = 8
    print(rod_cutting(length, price, n))

    length = [1,   2,   3,  4,   5,   6,   7,   8]
    price = [3,   5,   8,   9, 10,  17,  17,  20]
    n = 8
    print(rod_cutting(length, price, n))
