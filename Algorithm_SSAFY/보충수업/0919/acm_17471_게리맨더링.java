import java.util.Scanner;

//public class Main {
public class acm_17471_게리맨더링 {
	
	static int N;
	static int [] people;
	static int [][] G;
	static int ans = Integer.MAX_VALUE;
	static int [] subset;
	
	static int dfs(int v, int area[], int areacnt, int visited[])
	{
		int ret = people[v];
		visited[v] = 1;

		for (int u = 1; u <= G[v][0]; u++)
		{
			if (visited[G[v][u] - 1] == 1) continue;
			
			boolean found = false;
			for (int j = 0; j < areacnt; j++)
			{
				if (area[j] == (G[v][u] - 1))
				{
					found = true;
					break;
				}
			}
			
			if (found)
				ret += dfs(G[v][u] - 1, area, areacnt, visited);
		}

		return ret;
	}
	
	static void solve(int k)
	{
		if (k == N)
		{
			int tsum = 0;
			for (int i = 0; i < N; i++)
				tsum += subset[i];
			if (tsum == 0 || tsum == N) return;

			int [] area1 = new int [10];
			int t1 = 0;
			int [] area2 = new int [10];
			int t2 = 0;

			for (int i = 0; i < N; i++)	{
				if (subset[i] == 1)	area1[t1++] = i;
				else 			area2[t2++] = i;
			}
			
			int [] visited = new int [10];
			int v1 = dfs(area1[0], area1, t1, visited);
			int v2 = dfs(area2[0], area2, t2, visited);
					
			tsum = 0;
			for (int i = 0; i < N; i++)
				tsum += visited[i];
			if (tsum == N)
				ans = ans > Math.abs(v1 - v2) ? Math.abs(v1 - v2) : ans;
		}
		else
		{
			subset[k] = 1; solve(k + 1);
			subset[k] = 0; solve(k + 1);
		}
	}
	
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

    	N = sc.nextInt();
    	people = new int [N];
    	subset = new int [N];
    	
        for(int i = 0; i < N; i++)
        	people[i] = sc.nextInt();

        G = new int [N][10];
    	for (int i = 0; i < N; i++)	{
    		G[i][0] = sc.nextInt();
    		for (int j = 1; j <= G[i][0]; j++)
    			G[i][j] = sc.nextInt();
    	}

    	solve(0);
    	
    	if (ans == Integer.MAX_VALUE)	System.out.println(-1);
    	else			System.out.println(ans);

        sc.close();
    }

}
