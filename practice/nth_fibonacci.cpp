#include <bits/stdc++.h>
using namespace std;



int main()
{
    int a[10000],n;

    cin>>n;

    a[0]=0;
    a[1]=1;

    for(int i=2; i<n;i++)
        a[i]=a[i-1]+a[i-2];

    cout << a[n-1] <<" (";
    for(int i=0; i<n -1; i++)
        cout << a[i] <<", ";

    cout << a[n-1];
    cout << ")";

    cout << endl;

    return 0;

}
