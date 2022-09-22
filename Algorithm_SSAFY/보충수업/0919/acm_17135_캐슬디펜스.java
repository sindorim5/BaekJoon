import java.util.Scanner;

//public class Main {
public class acm_17135_캐슬디펜스 {
	
	static int N;
	static int M;
	static int D;
	static int ans, tans;
	static int [][] mat;
	static int [][] killed;
	static int [] archer = new int [3];
	static int [] Q = new int [100000];
	static int f = -1, r = -1;
	
	static void kill(int k, int y) {
		int xx = -1;
		int yy = -1;
		int min_d = 100;
		for(int i = k - 1; i > -1; i--) {
			for(int j = 0; j < M; j++) {
				if(mat[i][j] == 1 && killed[i][j] == 0) {
					int td = Math.abs(i - k) + Math.abs(j - y);
					if(td < min_d) {
						xx = i; yy = j; min_d = td;
					}
					else if(td == min_d && j < yy) {
						xx = i; yy = j;
					}
				}
			}
		}
		
		if(min_d <= D) {
			Q[++r] = xx;
			Q[++r] = yy;
		}
	}
	
	static void solve(int k) {
		if(k == 0) return;
		else {
			kill(k, archer[0]);
			kill(k, archer[1]);
			kill(k, archer[2]);
			while(f != r)
			{
				int x = Q[++f];
				int y = Q[++f];
				killed[x][y] = 1;
			}
			solve(k - 1);

		}
	}
	
	static int getKilled() {
		int tsum = 0;
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
            	if(killed[i][j] == 1)
            		tsum++;
        return tsum;
	}
	
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

    	N = sc.nextInt();
    	M = sc.nextInt();
    	D = sc.nextInt();
    	
    	mat = new int [N][M];

        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
            	mat[i][j] = sc.nextInt();
        
        ans = 0;
        
        for(int i = 0; i < M - 2; i++) {
        	for(int j = i + 1; j < M - 1; j ++) {
        		for(int k = j + 1; k < M; k++) {
        			killed = new int [N][M];
        			tans = 0;
        			archer[0] = i;
        			archer[1] = j;
        			archer[2] = k;
        			solve(N);
        			ans = Math.max(ans, getKilled());
        		}
        	}
        }
        
    	System.out.println(ans);
        sc.close();
    }
}