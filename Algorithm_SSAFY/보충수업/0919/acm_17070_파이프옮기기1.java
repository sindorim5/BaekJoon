import java.util.Scanner;

public class Main {
//public class acm_17070_파이프옮기기1 {
	
	static int N;
	static int [][] mat;
	static int ans;

	static boolean checkRight(int x, int y) {
		
		if (y + 1 < N && mat[x][y + 1] == 0)
			return true;
		return false;
	}
	
	static boolean checkDown(int x, int y) {
		
		if (x + 1 < N && mat[x + 1][y] == 0)
			return true;
		return false;
	}
	
	static boolean checkDigonal(int x, int y) {
		if (x + 1 < N && y + 1 < N && 
				mat[x + 1][y] == 0 && 
				mat[x][y + 1] == 0 && 
				mat[x + 1][y + 1] == 0)
			return true;
		return false;
	}
	
	static void solve(int x, int y, int d) // d : → 0, ↓ 1,  ↘ 2
	{
		if (x == N - 1 && y == N - 1)	ans++;

		if (d == 0)
		{
			if (checkRight(x, y)) solve(x, y + 1, 0);
			
			if (checkDigonal(x, y))	solve(x + 1, y + 1, 2);
		}

		if (d == 1)
		{
			if (checkDown(x, y)) solve(x + 1, y, 1);
			
			if (checkDigonal(x, y))	solve(x + 1, y + 1, 2);
		}
		
		if (d == 2)
		{
			if (checkRight(x, y)) solve(x, y + 1, 0);
			
			if (checkDown(x, y)) solve(x + 1, y, 1);
			
			if (checkDigonal(x, y))	solve(x + 1, y + 1, 2);
		}
	}
	
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

    	N = sc.nextInt();
    	mat = new int [N][N];

        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
            	mat[i][j] = sc.nextInt();

        solve(0, 1, 0);
        
    	System.out.println(ans);
        sc.close();
    }
}
