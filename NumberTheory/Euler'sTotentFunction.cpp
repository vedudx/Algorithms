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

  
// Stores prime numbers upto MAX - 1 values
const int MAX = 100001;
  
// Stores prime numbers upto MAX - 1 values
vector<ll> p;
  
// Finds prime numbers upto MAX-1 and
// stores them in vector p
void sieve()
{
    ll isPrime[MAX+1];
  
    for (ll i = 2; i<= MAX; i++)
    {
        // if prime[i] is not marked before
        if (isPrime[i] == 0)
        {
            // fill vector for every newly
            // encountered prime
            p.push_back(i);
  
            // run this loop till square root of MAX,
            // mark the index i * j as not prime
            for (ll j = 2; i * j<= MAX; j++)
                isPrime[i * j]= 1;
        }
    }
}
  
// function to find totient of n
ll phi(ll n)
{
    ll res = n;
  
    // this loop runs sqrt(n / ln(n)) times
    for (ll i=0; p[i]*p[i] <= n; i++)
    {
        if (n % p[i]== 0)
        {
            // subtract multiples of p[i] from r
            res -= (res / p[i]);
  
            // Remove all occurrences of p[i] in n
            //this is done so that we can know if there's a sneaky prime factor greater than sqrt(n)
            while (n % p[i]== 0)
               n /= p[i];
        }
    }
  
    // when n has prime factor greater
    // than sqrt(n)
    if (n > 1)
       res -= (res / n);
  
    return res;
}
  

int main()
{
ios_base::sync_with_stdio(false); cin.tie(NULL);  

int n;
cin >> n;
sieve();
cout << phi(n) << endl;
return 0;
}