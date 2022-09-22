import java.util.Scanner;

//public class Main {
public class acm_14888_연산자끼워넣기 {
	
	static int N;
	static int nums[];
	static int ops[] = new int [4];
	static int maxans;
	static int minans;
	
	public static void solve(int k, int v ) {
		
		if (k == N)
		{
			maxans = Math.max(maxans, v);
			minans = Math.min(minans, v);
		}
		 
		for (int i = 0; i < 4; i++) {
			if (ops[i] > 0) {
				ops[i]--;
				
				switch (i) {
					case 0 : solve(k + 1, v + nums[k]); break;
					case 1 : solve(k + 1, v - nums[k]); break; 
					case 2 : solve(k + 1, v * nums[k]); break;
					case 3 : solve(k + 1, v / nums[k]); break;
				}
				ops[i]++;
			}
		}
	}
	
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

    	N = sc.nextInt();
    	nums = new int [N];
    	
		for (int i = 0; i < N; i++)
			nums[i] = sc.nextInt();
		
    	for (int i = 0; i < 4; i++)
			ops[i] = sc.nextInt();
		
		maxans = Integer.MIN_VALUE;
		minans = Integer.MAX_VALUE;
        
		solve(1, nums[0]);
		
    	System.out.println(maxans);
    	System.out.println(minans);
    	
        sc.close();
    }

}