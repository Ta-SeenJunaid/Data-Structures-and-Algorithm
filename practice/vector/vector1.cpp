#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> my_vec;

    my_vec.push_back(5);
    my_vec.push_back(150);
    my_vec.push_back(455);

    cout << my_vec.size() <<endl;

    for(int i=0; i < my_vec.size(); i++)
        cout<< "vector element " << i << " value " << my_vec[i] << endl;


    return 0;
}
