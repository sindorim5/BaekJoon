import java.util.Scanner;

//public class Main {
public class acm_16234_인구이동 {
	
	static int N, L, R;
	static int [][] mat;
	static boolean [][] visited;
	static int dx[] = { 1, -1, 0, 0 };
	static int dy[] = { 0, 0, 1, -1 };
	static int [] qx = new int [10000];
	static int [] qy = new int [10000];
	static int f, r;
	static boolean moved;
	
	static void bfs(int x, int y){
		int xx, yy;
		f = r = -1;
		qx[++r] = x; qy[r] = y;
		visited[x][y] = true;

		while (f != r){
			x = qx[++f]; y = qy[f];

			for (int i = 0; i < 4; i++)	{
				xx = x + dx[i];
				yy = y + dy[i];
				
				if (xx < 0 || xx >= N || yy < 0 || yy >= N) continue;

				int t = Math.abs(mat[x][y] - mat[xx][yy]);
				
				if (!visited[xx][yy] && L <= t && t <= R){
					visited[xx][yy] = true;
					qx[++r] = xx; qy[r] = yy;
				}
			}
		}

		if (r > 0)	{
			int tsum = 0;
			for (int i = 0; i <= r; i++)
				tsum += mat[qx[i]][qy[i]];

			for (int i = 0; i <= r; i++)
				mat[qx[i]][qy[i]] = tsum / (r + 1);
			moved = true;
		}
	}
	
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

    	N = sc.nextInt();
    	L = sc.nextInt();
    	R = sc.nextInt();

    	mat = new int [N][N];
    	
    	for (int i = 0; i < N; i++)
    		for (int j = 0; j < N; j++)
    			mat[i][j] = sc.nextInt();
    	
    	int cnt = 0;
    	
    	while (true)
    	{
    		visited = new boolean [N][N];
    		moved = false;

    		for (int i = 0; i < N; i++)
    			for (int j = 0; j < N; j++)
    				if (!visited[i][j])	
    					bfs(i, j);

    		if (moved) cnt++;
    		else  break;
    	}
        
    	System.out.println(cnt);
        sc.close();
    }

}