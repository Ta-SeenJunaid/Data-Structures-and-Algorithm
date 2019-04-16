// Bismillahir Rahmanir Raheem
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int i,j,n,count;
    scanf("%d",&n);
    count=0;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            count+=1;
        }
    }

    printf("%d %d",n,count);
    return 0;
}
