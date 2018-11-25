// Bismillahir Rahmanir Raheem
#include <bits/stdc++.h>
using namespace std;
void insertion_sort(int a[], int n)
{
    int i,j,item;
    for(i=1;i<n;i++){
        item= a[i];
    j=i-1;
    while( j>=0 && a[j]> item )
    {
        a[j+1] = a[j];
        j--;
    }
    a[j+1]=item;

    }



}

int main()
{
    int a[1000],elements,x;
    scanf("%d",&elements);
    for(int i=0;i<elements;i++)
        scanf("%d",&a[i]);


   insertion_sort(a, elements);
    printf("\n");
   for(int i=0;i<elements;i++)
        printf("%d\n",a[i]);



     return 0;

}





