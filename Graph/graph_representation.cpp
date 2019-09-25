#include <bits/stdc++.h>
using namespace std;

void addEdge(vector<int> adl[], int u, int v){
    adl[u].push_back(v);
    // undirected graph.
    adl[v].push_back(u);
}


void printGraph(vector<int> adl[], int v){
    for(int i=0; i<v; i++){
         cout << "\n Adjacency list of vertex "
             << i << "\n head ";

             for(auto x : adl[i])
                cout << "-> " << x; 

            cout<<endl;
    }
}




int main()
{
    int v = 4;

    vector<int> adl[v];

    addEdge(adl, 0, 1);
    addEdge(adl, 0, 3);
    addEdge(adl, 1, 1);
    addEdge(adl, 2, 3);
    addEdge(adl, 2, 0);
    addEdge(adl, 2, 1);
    addEdge(adl, 3, 3);
    addEdge(adl, 3, 1);
    addEdge(adl, 3, 0);
    
    printGraph(adl, v); 

    return 0;
}
