// Bismillahir Rahmanir Raheem
#include <bits/stdc++.h>
using namespace std;

int binary_search(int a[],int n, int x)
{
    int mid,left,right;
    left=0;
    right=n-1;
    while(left <=right)
    {
        mid=(left+right)/2;
        if(a[mid]==x)
            return mid;
        if(a[mid]<x)
            left = mid+1;
        else
            right = mid -1;
    }

    return -1;
}

int main()
{
    int a[1000],elements,x;
    scanf("%d",&elements);
    for(int i=0;i<elements;i++)
        scanf("%d",&a[i]);


    scanf("%d",&x);

   int ans = binary_search(a,elements,x);
     if(ans==-1)
        printf("not found");
     else
        printf("%d",ans);

     return 0;

}

