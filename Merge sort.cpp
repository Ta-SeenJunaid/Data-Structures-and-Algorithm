// Bismillahir Rahmanir Raheem
#include <bits/stdc++.h>
using namespace std;

void merge(int A[], int left, int mid, int right)
{
    int i,j,k;
    //int index_a, index_l, index_r;

    int size_left = mid-left+1;
    int size_right = right - mid;

    int L[size_left], R[size_right];

    for(i= 0; i<size_left; i++){
        L[i] = A[left+i];
    }
    for(j= 0; j< size_right; j++){
        R[j] = A[mid+1+j];
    }

    i=0;
    j=0;
    k=left;

    while(i<size_left && j<size_right){
        if(L[i]<=R[j]){
            A[k]= L[i];
            i++;
        }
        else{
            A[k] = R[j];
            j++;
        }
       k++;
    }
         /* Copy the remaining elements of L[], if there
       are any */
    while (i<size_left)
    {
        A[k] = L[i];
        i++;
        k++;
    }

    /* Copy the remaining elements of R[], if there
       are any */
    while (j<size_right)
    {
        A[k] = R[j];
        j++;
        k++;
    }

}

void merge_sort(int A[], int left, int right)
{
    if(left >= right){
        return;
    }

    int mid = left + (right - left)/2;

    merge_sort(A, left, mid);
    merge_sort(A, mid+1, right);

    merge(A, left, mid, right);

}



int main()
{
    int i, n=8;
    int A[] = {1,5,6,3,5,8,7,2,9};

    merge_sort(A, 0, n);
    for(i=0;i<=n;i++)
        printf("%d ", A[i]);

    printf("\n");

    return 0;
}
