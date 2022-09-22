import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day10_1949_등산로조성 {
     
    static int N;
    static int K;
    static int[][] map;
    static boolean[][] visited;
    static boolean usedk;
    static int ans;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    

    public static void dfs1(int x, int y, int h, int pathl)
    {
    	ans = Math.max(ans, pathl);

    	for (int i = 0; i < 4; i++)
    	{
    		int newx = x + dx[i];
    		int newy = y + dy[i];

    		if (newx < 0 || newx >= N || newy < 0 || newy >= N) continue;
    		if (visited[newx][newy]) continue;

    		visited[newx][newy] = true;

    		if (map[newx][newy] < h)
    			dfs1(newx, newy, map[newx][newy], pathl + 1);

    		visited[newx][newy] = false;
    	}
    }
    
    public static void dfs2(int x, int y, int h, int pathl)
    {
        ans = Math.max(ans, pathl);

        for (int i = 0; i < 4; i++)
        {
            int newx = x + dx[i];
            int newy = y + dy[i];

            if (newx < 0 || newx >= N || newy < 0 || newy >= N) continue;
            if (visited[newx][newy]) continue;

            visited[newx][newy] = true;

            if (map[newx][newy] < h)
                dfs2(newx, newy, map[newx][newy], pathl + 1);
            else if (!usedk && map[newx][newy] - K < h)
            {
                usedk = true;
                dfs2(newx, newy, h - 1, pathl + 1);
                usedk = false;
            }

            visited[newx][newy] = false;
        }
    }
    
    public static void main(String[] args) throws FileNotFoundException {
//    	System.setIn(new FileInputStream("day10_1949_등산로조성.txt"));
        Scanner sc = new Scanner(System.in);
         
        int TC = sc.nextInt();
         
        for (int tc = 1; tc <= TC; tc++) {
             
            N = sc.nextInt();
            K = sc.nextInt();
            map = new int[N][N];
            visited = new boolean[N][N];
             
            int highest = 0;
            
    		for (int i = 0; i < N; i++)
    			for (int j = 0; j < N; j++)
    			{
    				map[i][j] = sc.nextInt();
    				if (highest < map[i][j])
    					highest = map[i][j];
    			}
            

    		ans = 0; 
    		for (int i = 0; i < N; i++)
    			for (int j = 0; j < N; j++)
    			{
    				if (map[i][j] == highest)
    				{
    					visited[i][j] = true;
    					dfs1(i, j, highest, 1);
    					visited[i][j] = false;
    				}
    			}
    		
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                {
                    if (map[i][j] == highest)
                    {
                        visited[i][j] = true;
                        dfs2(i, j, highest, 1);
                        visited[i][j] = false;
                    }
                }
            
            System.out.println("#" + tc + " " + ans);
        }
        sc.close();
    }
}





//import java.io.FileInputStream;
//import java.io.FileNotFoundException;
//import java.util.Scanner;
//
//public class day10_1949_등산로조성 {
//     
//    static int N;
//    static int K;
//    static int[][] map;
//    static boolean[][] visited;
//    static int ans;
//    static int[] dx = {-1, 1, 0, 0};
//    static int[] dy = {0, 0, -1, 1};
//    
//
//    public static void dfs(int x, int y, int h, int pathl, boolean usedk)
//    {
//        ans = Math.max(ans, pathl);
//
//        for (int i = 0; i < 4; i++)
//        {
//            int newx = x + dx[i];
//            int newy = y + dy[i];
//
//            if (newx < 0 || newx >= N || newy < 0 || newy >= N) continue;
//            if (visited[newx][newy]) continue;
//
//            visited[newx][newy] = true;
//
//            if (map[newx][newy] < h)
//                dfs(newx, newy, map[newx][newy], pathl + 1, usedk);
//            else if (!usedk && map[newx][newy] - K < h)
//                dfs(newx, newy, h - 1, pathl + 1, true);
//
//            visited[newx][newy] = false;
//        }
//    }
//    
//    public static void main(String[] args) throws FileNotFoundException {
//        System.setIn(new FileInputStream("day10_1949_등산로조성.txt"));
//        Scanner sc = new Scanner(System.in);
//         
//        int TC = sc.nextInt();
//         
//        for (int tc = 1; tc <= TC; tc++) {
//             
//            N = sc.nextInt();
//            K = sc.nextInt();
//            map = new int[N][N];
//            visited = new boolean[N][N];
//             
//            int highest = 0;
//            
//            for (int i = 0; i < N; i++)
//                for (int j = 0; j < N; j++)
//                {
//                    map[i][j] = sc.nextInt();
//                    if (highest < map[i][j])
//                        highest = map[i][j];
//                }
//            
//
//            ans = 0; 
//            for (int i = 0; i < N; i++)
//                for (int j = 0; j < N; j++)
//                {
//                    if (map[i][j] == highest)
//                    {
//                        visited[i][j] = true;
//                        dfs(i, j, highest, 1, false);
//                        visited[i][j] = false;
//                    }
//                }
//            
//
//            System.out.println("#" + tc + " " + ans);
//        }
//        sc.close();
//    }
//}


