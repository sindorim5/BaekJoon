import java.util.Scanner;

//public class Main {
public class acm_14501_Επ»η {
	static int N;
	static int ans = 0;
	static int [] Ti = new int [15];
	static int [] Pi = new int [15];
	static boolean [] Si = new boolean [15];
	
	static void solve(int k)
	{
		if (k == N)
		{
			for (int i = 0; i < N; i++)
			{
				if (Si[i])
					for (int j = i + 1; j < i + Ti[i]; j++)
						if (j >= N || Si[j])
							return;
			}
			int tsum = 0;
			for (int i = 0; i < N; i++)
				if (Si[i])
					tsum += Pi[i];
			if (tsum > ans) ans = tsum;
		}
		else
		{
			Si[k] = true;
			solve(k + 1);
			Si[k] = false;
			solve(k + 1);
		}
	}
	
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

    	N = sc.nextInt();

        for(int i = 0; i < N; i++) {
        	Ti[i] = sc.nextInt();
        	Pi[i] = sc.nextInt();
        }

        solve(0);
        
    	System.out.println(ans);
        sc.close();
    }

}
