// Bismillahir Rahmanir Raheem
#include <bits/stdc++.h>
using namespace std;

int linear_search(int a[],int n, int x)
{
    for(int i=0;i<n;i++){
        if(a[i]==x)
            return i;
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

   int ans = linear_search(a,elements,x);
     if(ans==-1)
        printf("not found");
     else
        printf("%d",ans);

     return 0;

}
