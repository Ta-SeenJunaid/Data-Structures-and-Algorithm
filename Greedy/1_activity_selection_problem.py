
def printMaxActivities(s, f):
    n = len(f)

    i = 0
    print(i, " ")

    for j in range(1,n):
        if f[i] <= s[j]:
            i=j
            print(i, " ")


s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
printMaxActivities(s , f)