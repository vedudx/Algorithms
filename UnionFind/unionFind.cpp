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
int main()
{
ios_base::sync_with_stdio(false); cin.tie(NULL); 
int N, Q;
cin >> N >> Q;
UnionFind<int>uf;

while (Q--)
{
    char a;
    int b , c;
    cin >> a >> b >> c;
    uf.insert(b);
    uf.insert(c);
    if (a == '=')
    {
        uf.merge(b,c);
    }
    else
    {
        if (uf.root(b) == uf.root(c))
            cout << "yes\n";
        else
            cout << "no\n";
    }   
}
return 0;
}