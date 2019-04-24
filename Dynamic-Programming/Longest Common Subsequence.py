# -*- coding: utf-8 -*-

def lcs(x,y):
    m=len(x)
    n=len(y)
    
    l=[[None]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=1+l[i-1][j-1]
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])

    return l[m][n]

x=input("Enter 1st string: ")
y=input("Enter 2nd string: ")

print("LCS of 1st & 2nd string is: ",lcs(x,y))