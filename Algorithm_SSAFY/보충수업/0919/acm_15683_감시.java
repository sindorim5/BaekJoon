import java.util.Scanner;

//public class Main {
public class acm_15683_감시 {
    
    static int N, M;
    static int ans;
    static int [][] mat;
    static boolean [][] visited;
    static int [][] cctvXYC = new int [8][3]; // type, x, y
    static int cctvCnt = 0;
    static int [] direction;
    
     public static void fill_right(int x, int y, boolean tvisited[][]) {
        int yy = y + 1;
        while (yy < M && mat[x][yy] != 6) 
            tvisited[x][yy++] = true; 
     }
        
     public static void fill_left(int x, int y, boolean tvisited[][]) {
            int yy = y - 1;
            while (yy > -1 && mat[x][yy] != 6) 
                tvisited[x][yy--] = true; 
     }
                    
     public static void fill_up(int x, int y, boolean tvisited[][]) {
            int xx = x + 1;
            while (xx < N && mat[xx][y] != 6) 
                tvisited[xx++][y] = true; 
     }

     public static void fill_down(int x, int y, boolean tvisited[][]) {
            int xx = x - 1;
            while ( xx > -1 && mat[xx][y] != 6) 
                tvisited[xx--][y] = true; 
     }
        
     public static void observe() {
        boolean [][] tvisited = new boolean [N][M];
        
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                tvisited[i][j] = visited[i][j];

        for (int i = 0; i < cctvCnt; i++) {
            int cctvC = cctvXYC[i][0];
            int x = cctvXYC[i][1];
            int y = cctvXYC[i][2];
            
            int dir = direction[i];
            
            tvisited[x][y] = true;
            
            if (cctvC == 1) {
                if (dir == 0)   fill_right(x, y, tvisited);
                else if( dir == 1) fill_down(x, y, tvisited);
                else if( dir == 2) fill_left(x, y, tvisited);
                else if( dir == 3) fill_up(x, y, tvisited);
            }
            else if( cctvC == 2) {
                if (dir == 0) {
                    fill_right(x, y, tvisited);
                    fill_left(x, y, tvisited);
                }
                else if(dir == 1) {
                    fill_up(x, y, tvisited);
                    fill_down(x, y, tvisited);
                }
            }
            else if(cctvC == 3) {
                if (dir == 0) {
                    fill_up(x, y, tvisited);
                    fill_right(x, y, tvisited);
                }
                else if(dir == 1) {
                    fill_right(x, y, tvisited);
                    fill_down(x, y, tvisited);
                }
                else if (dir == 2) {
                    fill_down(x, y, tvisited);
                    fill_left(x, y, tvisited);
                }
                else if (dir == 3) {
                    fill_left(x, y, tvisited);
                    fill_up(x, y, tvisited);
                }
            }
            else if (cctvC == 4) {
                if (dir == 0) {
                    fill_right(x, y, tvisited);
                    fill_left(x, y, tvisited);
                    fill_up(x, y, tvisited);
                }
                else if (dir == 1) {
                    fill_right(x, y, tvisited);
                    fill_down(x, y, tvisited);
                    fill_up(x, y, tvisited);
                }
                else if (dir == 2) {
                    fill_right(x, y, tvisited);
                    fill_down(x, y, tvisited);
                    fill_left(x, y, tvisited);
                }
                else if (dir == 3) {
                    fill_down(x, y, tvisited);
                    fill_left(x, y, tvisited);
                    fill_up(x, y, tvisited);
                }
            }
        }
            
        int tsum = 0;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                if(tvisited[i][j]) tsum++;
                    
        ans = ans < tsum ? tsum : ans;
     }
            
    
     public static void solve(int k) {
        if( k == cctvCnt)
            observe();
        else{
            if (cctvXYC[k][0] == 2) {
                for (int i = 0; i < 2; i++) {
                    direction[k] = i;
                    solve(k + 1);
                }
            }
            else{
                for (int i = 0; i < 4; i++) {
                    direction[k] = i;
                    solve(k + 1);
                }
            }
        }
     }
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        mat = new int [N][M];
        visited = new boolean [N][M];
        
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                mat[i][j] = sc.nextInt();
        
        for(int x = 0; x < N; x++) {
            for(int y = 0; y < M; y++) {
                if (mat[x][y] == 0) 
                    continue;
                else if( mat[x][y] == 6)
                    visited[x][y] = true;
                else if (mat[x][y] == 5) {
                    visited[x][y] = true;
                    fill_right(x, y, visited);
                    fill_left(x, y, visited);
                    fill_up(x, y, visited);
                    fill_down(x, y, visited);
                }
                else {
                    cctvXYC[cctvCnt][0] = mat[x][y];
                    cctvXYC[cctvCnt][1] = x;
                    cctvXYC[cctvCnt++][2] = y;
                }
            }
        }
        ans = 0;
        direction = new int [cctvCnt];
        solve(0);
       
        System.out.println(N*M - ans);
        sc.close();
    }
    
}
