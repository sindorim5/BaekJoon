import java.util.Scanner;

//public class Main {
public class acm_14889_스타트와링크 {
	
	static int N;
	static int R;
	static int [][] mat;
	static int [] team;
	static int ans = 0x7fffffff;
	
	static void solve(int k, int s)
	{
		if (k == R)
		{
			int start = 0, link = 0;

			int [] chk = new int [20];
			int [] x = new int [20];

			for (int i = 0; i < R; i++)
				chk[team[i]] = 1;
			int tcnt = 0;
			for (int i = 0; i < 20; i++)
				if (chk[i] == 0)
					x[tcnt++] = i;

			for (int i = 0; i < R - 1; i++)
				for (int j = i + 1; j < R; j++)
					start += (mat[team[i]][team[j]] + mat[team[j]][team[i]]);

			for (int i = 0; i < R - 1; i++)
				for (int j = i + 1; j < R; j++)
					link += (mat[x[i]][x[j]] + mat[x[j]][x[i]]);

			ans = ans < Math.abs(start - link) ? ans : Math.abs(start - link);
		}
		else
			for (int i = s; i < N + (k - R) + 1; i++)
			{
				team[k] = i;
				solve(k + 1, i + 1);
			}
	}
	
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

    	N = sc.nextInt();
    	mat = new int [N][N];

    	R = N / 2;
    	team = new int [R];

        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
            	mat[i][j] = sc.nextInt();

        solve(0, 0);
        
    	System.out.println(ans);
        sc.close();
    }

}