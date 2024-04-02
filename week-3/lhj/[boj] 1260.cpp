#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <vector>
#include <limits.h>
#include<queue>
using namespace std;

int arr[1001][1001];
int check[1001];
int n;

void dfs(int v)
{
    check[v] = 1;  
    cout << v << " ";

    for (int i = 1; i <= n; i++)
    {
        if (arr[v][i] == 2 && check[i] == 0)
        {
            dfs(i); 
        }
        if (i == n)
            return;
    }
}

void bfs(int v) {
    queue<int>q;
    q.push(v);
    check[v] = true;
    cout << v << " ";

    while (!q.empty()) {
        v = q.front();
        q.pop();

        for (int i = 1; i <= n; i++) {
            if (arr[v][i] == 2 && check[i] == 0) { //현재 정점과 연결되어있고 방문되지 않았으면
                q.push(i);
                check[i] = true;
                cout << i << " ";
            }
        }
    }
}

int main() {
	int m, v;
	cin >> n >> m >> v;

	for (int i = 0; i < m; i++) {
		int a, b, v;
		cin >> a >> b;
		arr[a][b] = 2;
		arr[b][a] = 2;
	}

	dfs(v);
    cout << "\n";

    for (int i = 1; i <= n; i++) {
        check[i] = 0;
    }

    bfs(v);
}