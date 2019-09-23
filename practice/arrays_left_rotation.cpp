/*
A left rotation operation on an array shifts each of the array's elements unit to the left. For example, if left rotations are performed on array , then the array would become

.

Given an array
of integers and a number, , perform

left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

    An array of integers 

.
An integer

    , the number of rotations.

Input Format

The first line contains two space-separated integers
and , the size of and the number of left rotations you must perform.
The second line contains space-separated integers

.

Constraints

Output Format

Print a single line of
space-separated integers denoting the final state of the array after performing left rotations.
*/

#include <bits/stdc++.h>
using namespace std;

int array_left(int n,int d, int a[])
{
    for(int i=d; i <n;i++)
        cout << a[i] << endl;

    for(int i=0; i<d; i++)
        cout << a[i] << endl;
}

int main()
{
    int n,d, a[100002];


    cout << "Input n: "<< endl;
    cin >> n;

    cout << "Input d: "<< endl;
    cin >> d;

    cout << "Input array: "<< endl;
    for(int i=0; i<n; i++)
        cin >> a[i];

    cout << "Output: "<< endl;    
    array_left(n, d, a);


    return 0;
}
