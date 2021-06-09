#include <bits/stdc++.h>  
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)
typedef long double lld;
typedef pair<int,int>pii;
#define f first
#define s second
#define mp make_pair
typedef unsigned long long ull;
typedef long long ll;

template<typename T>
struct edge
{
    T dst;
    T src;
    int wt;

};
template<typename T>
class UnionFind{
public:
    unordered_map<T, T> uf;
    unordered_map<T, int> size;
    UnionFind(){}
    
    void insert(T a)
    {
        if (uf.count(a) == 0)
        {
            uf[a] = a;
            size[a] = 1;
        }

    }
    T root(T i) 
    {
        while(i != uf[i])
        {
            i = uf[i];
            uf[i] = uf[uf[i]];
        }
        return i;
    }
    int merge(T p, T q)
    {
        T a = root(p);
        T b = root(q);
        if (a == b)
            return size[a];
        if (size[a] < size[b])
        {
            uf[a] = b;
            size[b] += size[a];
            return size[b];
        }
        else
        {
                uf[b] = a;
                size[a] += size[b];
                return size[a];
        }
    }
};

bool compareWeights (edge<int> a, edge<int> b){
if(a.wt < b.wt) return true ;
else return false ;
}

int main()
{
ios_base::sync_with_stdio(false); cin.tie(NULL); 
int N;
cin >> N;
UnionFind<int>uf;
vector<edge<int>>edges;
// take the input here
// add edges and nodes to unionfind
sort(edges.begin(), edges.end(), compareWeights);

int minCost = 0;
for (auto e: edges)
{ 
    int p = uf.root(e.src);
    int q = uf.root(e.dst);
    if (p == q)
        continue;
    uf.merge(p, q);
    cout << e.src << " " << e.dst << endl;
    minCost += e.wt;
}


return 0;
}