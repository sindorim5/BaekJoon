import java.util.Scanner;

//public class Main {
public class acm_15686_치킨배달 {
	
	static int N, M;
	static int [][] mat;
	static int [][] home = new int [100][2];
	static int homecnt;
	static int [][] chicken = new int [13][2];
	static int chickencnt;
	static int [][] dist = new int [13][100];
	static int ans = Integer.MAX_VALUE;
	static int [] combi = new int [13];
	
	static void solve(int k, int s){
		
		if (k == M){
			int tsum = 0;
			for (int h = 0; h < homecnt; h++){
				int tmin = Integer.MAX_VALUE;
				for (int c = 0; c < M; c++)
					tmin = Math.min(tmin, dist[combi[c]][h]);
				tsum += tmin;
			}
			ans = Math.min(ans,  tsum);
		}
		else
			for (int i = s; i < chickencnt + k - M + 1; i++){
				combi[k] = i;
				solve(k + 1, i + 1);
			}
	}
	
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

    	N = sc.nextInt();
    	M = sc.nextInt();
    	
    	mat = new int [N][N];

        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
            	mat[i][j] = sc.nextInt();

    	for (int i = 0; i < N; i++)	{
    		for (int j = 0; j < N; j++)	{
    			
    			if (mat[i][j] == 1)	{
    				home[homecnt][0] = i;
    				home[homecnt++][1] = j;
    			}
    			else if (mat[i][j] == 2) {
    				chicken[chickencnt][0] = i;
    				chicken[chickencnt++][1] = j;
    			}
    		}
    	}
        
    	for (int i = 0; i < chickencnt; i++)
    		for (int j = 0; j < homecnt; j++)
    			dist[i][j] = Math.abs(chicken[i][0] - home[j][0]) + 
    						 Math.abs(chicken[i][1] - home[j][1]);
    	
        solve(0, 0);
        
    	System.out.println(ans);
        sc.close();
    }

}