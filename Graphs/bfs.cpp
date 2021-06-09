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
class Graph {
public:
	unordered_map<T, unordered_map<T, int> > adj;
    int len = 0, maxLen = 0; 
    T farthNode;
	//map<int,bool>visited; //global visited which you can remove and just have one in dfs if u have to check connectivity only between two edges
	Graph() {} // constructor
	void addEdge(T u, T v, int wt, bool bidir = true) {
		adj[u][v] = wt; // you have added an edge from u - v with weight wt
		if(bidir) {
			adj[v][u] = wt;
		}
	}
 
	void printAdj() {
		for(auto row : adj) {
			cout<<row.first<<" := ";
			for(auto neighbour : row.second) {
				cout<<"("<<neighbour.first<<","<<neighbour.second<<") -> ";
			}
			cout<<endl;
		}
	}
    void bfs(T src) {
		queue<T> q;
        map<T, bool> visited; 

		q.push(src);
		visited[src] = true;

		while(!q.empty()) {
			T node = q.front();
			cout<<node<<" ";
			q.pop();
			for(auto neighbour: adj[node]) {
				if(!visited[neighbour.first]) {
					q.push(neighbour.first);
					visited[neighbour.first] = true;
				}
			}
		}
	}
     void dfsHelper(T src, map<T, bool> &visited) {
     	visited[src] = true;
     	for(auto neighbour : adj[src]) {
     		if(!visited[neighbour.first]) {
                len++;
     			dfsHelper(neighbour.first, visited);
                len--;
     		}
     	}
         if (len > maxLen)
         {
             maxLen = len;
             farthNode = src;
         }
     }
 
     int dfs(T src) {
     	map<T, bool> visited; 
		 //whenever dfs is called this visited map will be initialised
     	dfsHelper(src, visited);
         return (visited.size());
     }
 
	//  bool visit(T src)
	//  {
	// 	 return visited[src];
	//  }
};

int main()
{

    Graph<int> g;
	g.addEdge(0, 1,-1,false);
	g.addEdge(1, 3,-1,false);
	g.addEdge(1, 2,-1,false);
	g.addEdge(0, 2,-1,false);
	
	// g.printAdjList();
	g.bfs(0);
    g.printAdj();
    
}