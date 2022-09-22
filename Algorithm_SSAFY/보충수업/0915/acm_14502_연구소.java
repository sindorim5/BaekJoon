import java.util.Scanner;

//public class Main {
public class acm_14502_??? {

	static int N, M;
	static int [][] mat;
	static int [][] backup_mat;
	static int [][] virus_pos = new int [10][2];
	static int viruscnt;
	static int [][] safe_pos = new int [64][2];
	static int safecnt = 0;
	static int ans;
	static int [] combi = new int [10];
	
	static void virus_infact(int x, int y)
	{
		mat[x][y] = 2;
		int dx[] = { 0, 0, 1, -1 };
		int dy[] = { 1, -1, 0, 0 };
		int xx, yy;

		for (int i = 0; i < 4; i++)
		{
			xx = x + dx[i];
			yy = y + dy[i];
			if (xx < 0 || xx >= N || yy < 0 || yy >= M) continue;
			if (mat[xx][yy] == 0)
				virus_infact(xx, yy);
		}
	}
	
	static void solve(int k, int s)
	{
		if (k == 3)
		{
			int x, y;

			for (int i = 0; i < 3; i++)
			{
				x = safe_pos[combi[i]][0];
				y = safe_pos[combi[i]][1];
				mat[x][y] = 1;
			}

			for (int i = 0; i < viruscnt; i++)
			{
				x = virus_pos[i][0];
				y = virus_pos[i][1];
				virus_infact(x, y);
			}

			int tsafecnt = 0;
			for (int i = 0; i < N; i++)
				for (int j = 0; j < M; j++)
					if (mat[i][j] == 0)
						tsafecnt++;
			if (ans < tsafecnt) ans = tsafecnt;

			for (int i = 0; i < N; i++)
				for (int j = 0; j < M; j++)
					mat[i][j] = backup_mat[i][j];
		}
		else
		{
			for (int i = s; i < safecnt + (k - 3) + 1; i++)
			{
				combi[k] = i;
				solve(k + 1, i + 1);
			}
		}
	}
	
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

    	N = sc.nextInt();
    	M = sc.nextInt();
    	
    	mat = new int [N][M];
    	backup_mat = new int [N][M];

    	for (int i = 0; i < N; i++)
    		for (int j = 0; j < M; j++)
    			backup_mat[i][j] = mat[i][j] = sc.nextInt();
    		
    	for (int i = 0; i < N; i++)	{
    		for (int j = 0; j < M; j++)	{
    			
    			if (mat[i][j] == 2)	{
    				virus_pos[viruscnt][0] = i;
    				virus_pos[viruscnt++][1] = j;
    			}
    			else if (mat[i][j] == 0){
    				safe_pos[safecnt][0] = i;
    				safe_pos[safecnt++][1] = j;
    			}
    		}
    	}

        solve(0, 0);
        
    	System.out.println(ans);
        sc.close();
    }
}