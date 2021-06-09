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
vector<vector<char>>mapp;

void flood(int i, int j, int r, int c)
{   
    if (mapp[i] [j] == '#')
        return;
    
    mapp[i] [j] = '#';
    if (i > 0)
        flood(i-1, j, r, c);
    if (i < r - 1)
        flood(i+1, j, r , c);
    if (j > 0)
        flood(i, j-1, r, c);
    if(j < c - 1)
        flood(i, j+1, r, c);
}

void print(vector<vector<char>>&mapp, int r, int c)
{
    for(auto i = 0; i < r; ++i)
    {
        for(auto j = 0; j < c; ++j)
        {
            cout << mapp[i] [j] << " ";
        }
        cout << "\n";
    }
}
int main()
{
ios_base::sync_with_stdio(false); cin.tie(NULL); 
int r, c;
cin >> r >> c;
unordered_map<string, unordered_map<string, bool>> seen;
rep(i,0,r)
{
    vector<char> row(c);
    for (auto &a: row)
    {
        cin >> a;
    }
    mapp.push_back(row);
}

print(mapp, r, c);
int cnt = 0;
for(auto i = 0; i < r; ++i)
{
    for(auto j = 0; j < c; ++j)
    {
        if (mapp[i] [j] == '-')
        {
            flood(i,j, r, c); cnt++;//cout << endl;
        }
    }
}
cout << cnt << endl;
return 0;
}