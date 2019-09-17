/*
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
*/

#include <bits/stdc++.h>
using namespace std;

int subarraySum(int l, int k, int a[]){
    int count = 0, sum;

    for(int i =0; i<l; i++){
        sum = a[i];

        for(int j=i+1; j<l ; j++){
            sum = sum + a[j];
            //cout << sum;
            if(sum == k){
                count++;
                break;
            }
            else if(sum > k)
                break;
            
        }
    }    

    return count;

}




int main()
{
    int k, l, a[1000], count=0, sum;
    
    cout << "Enter the length of array: "<<endl;
    cin >> l;

    cout << "Enter the elements of array: "<<endl;
    for(int i=0; i<l; i++)
        cin >> a[i];
    
    cout << "Enter k: "<<endl;
    cin >> k;
    
    int ans = subarraySum(l,k,a);
    cout <<"Answer is: "<<ans<<endl;

    return 0;
}