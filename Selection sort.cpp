// Bismillahir Rahmanir Raheem
#include <bits/stdc++.h>
using namespace std;
void selection_sort(int a[], int n)
{
    int i,j,index_min,temp;
    for(int i=0; i<n-1; i++){
         index_min=i;
         for(j=i+1;j<n;j++){
                if(a[j]<a[index_min])
                   index_min=j;

         }
         if(index_min!= i){
            temp=a[i];
            a[i]=a[index_min];
            a[index_min]= temp;
         }
    }


}

int main()
{
    int a[1000],elements,x;
    scanf("%d",&elements);
    for(int i=0;i<elements;i++)
        scanf("%d",&a[i]);


   selection_sort(a, elements);
    printf("\n");
   for(int i=0;i<elements;i++)
        printf("%d\n",a[i]);



     return 0;

}


