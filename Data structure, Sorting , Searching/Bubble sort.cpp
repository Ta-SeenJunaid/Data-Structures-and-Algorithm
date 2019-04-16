// Bismillahir Rahmanir Raheem
#include <bits/stdc++.h>
using namespace std;
void bubble_sort(int a[], int n)
{
    int i,j,temp;
    for(i=0;i<n;i++){
        for(j=0;j<n-i-1;j++){//for(j=0;j<n-1;j++) tjis is also valid
            if(a[j]>a[j+1]){
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }


}

int main()
{
    int a[1000],elements,x;
    scanf("%d",&elements);
    for(int i=0;i<elements;i++)
        scanf("%d",&a[i]);


   bubble_sort(a, elements);
    printf("\n");
   for(int i=0;i<elements;i++)
        printf("%d\n",a[i]);



     return 0;

}




