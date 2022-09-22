//import java.io.FileInputStream;
//import java.io.FileNotFoundException;
//import java.util.Scanner;
//
//public class day12_1249_보급로 {
//	public static int M[][] ;
//	public static int D[][] ;
//	public static int N;
//	public static int dx[] = { 0, 0, 1, -1 };
//	public static int dy[] = { 1, -1, 0, 0 };
//	
//	public static void solve()
//	{
//
//		 int x, y, min, curx = 0, cury = 0;
//	
//		 D[1][1] = 0;
//	
//		 while (true)
//		 {
//			 min = 0x7FFFFFFF;
//			 
//			 for (int i = 1; i <= N; i++)
//				 for (int j = 1; j <= N; j++)
//					 if (M[i][j] != -1 && D[i][j] < min)
//					 {
//						 	min = D[i][j];
//						 	curx = i;
//						 	cury = j;
//					 }
//	
//			 if (curx == N && cury == N) return;
//			 
//			 M[curx][cury] = -1;
//	
//			 for (int i = 0; i < 4; i++)
//			 {
//				  x = curx + dx[i];
//				  y = cury + dy[i];
//				  if (M[x][y] == -1) continue;
//				  if (D[x][y] > min + M[x][y]) D[x][y] = min + M[x][y];
//			 }
//		 }
//	}
//
//
//	public static void main(String[] args) throws FileNotFoundException {
//		
//		long start = System.currentTimeMillis();
//		
//		System.setIn(new FileInputStream("day12_1249_input.txt"));
//        Scanner sc = new Scanner(System.in);
//
//    	int TC = sc.nextInt();
//    	
//        for(int tc = 1; tc <= TC; tc++) {
//        	
//        	N = sc.nextInt();
//        	
//        	M = new int [N + 2][N + 2];
//        	D = new int [N + 2][N + 2];
//
//        	sc.nextLine();
//			for (int i = 1; i <= N; i++)
//			{
//				String str = sc.nextLine();
//        		for (int j = 1; j <= N; j++)
//        		{
//        			M[i][j] = str.charAt(j - 1) - '0';
//        		    D[i][j] = 0x7FFFFFFF;
//        		}
//			}
//
//        	solve();
//        	
//     		System.out.printf("#%d %d\n", tc, D[N][N]);
//
//	    }
//        System.out.println(( System.currentTimeMillis() - start )/1000.0 ); 
//        sc.close();
//	}
//}



import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day12_1249_보급로 {
    public static int M[][] ;
    public static int D[][] ;
    public static int N, heapSz, curX, curY;
    public static int heap[][] = new int [10000][2]; // x, y
    public static int dx[] = { 0, 0, 1, -1 };
    public static int dy[] = { 1, -1, 0, 0 };
    
    
    public static void push(int x, int y)
    {
      heapSz++;

      heap[heapSz][0] = x;
      heap[heapSz][1] = y;

      int cur = heapSz;

      while (cur > 1 && D[ heap[cur][0] ][ heap[cur][1] ] < D[ heap[cur / 2][0] ][ heap[cur / 2][1] ])
      {
          int tx = heap[cur / 2][0], ty = heap[cur / 2][1];
          heap[cur / 2][0] = heap[cur][0]; heap[cur / 2][1] = heap[cur][1];
          heap[cur][0] = tx; heap[cur][1] = ty;
          cur = cur / 2;
      }
    }
    
    
    public static void pop()
    {
      curX = heap[1][0]; curY = heap[1][1]; // heap의 루트 값 pop

      heap[1][0] = heap[heapSz][0]; heap[1][1] = heap[heapSz][1];

      heapSz--;

      int cur = 1;

      while (cur * 2 <= heapSz)
      {
          int child;
          if (cur * 2 == heapSz)
          {
              child = cur * 2;
          }
          else
          {
              if (D[ heap[cur * 2][0] ][ heap[cur * 2][1] ] < D[ heap[cur * 2 + 1][0] ][ heap[cur * 2 + 1][1] ])
                  child = cur * 2;
              else
                  child = cur * 2 + 1;
          }

          if (D[ heap[cur][0] ][ heap[cur][1] ]  < D[ heap[child][0] ][ heap[child][1] ]) break;

          int tx = heap[cur][0], ty = heap[cur][1];
          heap[cur][0] = heap[child][0]; heap[cur][1] = heap[child][1];
          heap[child][0] = tx; heap[child][1] = ty ;

          cur = child;
      }
    }
    
    public static void solve()
    {

         int x, y, min;
    
         D[1][1] = 0;
    
         push(1, 1);

         while (true)
         {
             pop();

             min = D[curX][curY];

             if (curX == N && curY == N) return;

             M[curX][curY] = -1;

             for (int i = 0; i < 4; i++)
             {
                 x = curX + dx[i];
                 y = curY + dy[i];
                 if (M[x][y] == -1) continue;
                 if (D[x][y] > min + M[x][y])
                 {
                     D[x][y] = min + M[x][y];
                     push(x, y);
                 }
             }
         }
    }


    public static void main(String[] args) throws FileNotFoundException {
        
        long start = System.currentTimeMillis();
        
        System.setIn(new FileInputStream("day12_1249_input.txt"));
        Scanner sc = new Scanner(System.in);

        int TC = sc.nextInt();
        
        for(int tc = 1; tc <= TC; tc++) {
            
            N = sc.nextInt();
            
            heapSz = 0;
            
            M = new int [N + 2][N + 2];
            D = new int [N + 2][N + 2];

            sc.nextLine();
            for (int i = 1; i <= N; i++)
            {
                String str = sc.nextLine();
                for (int j = 1; j <= N; j++)
                {
                    M[i][j] = str.charAt(j - 1) - '0';
                    D[i][j] = 0x7FFFFFFF;
                }
            }

            solve();
            
            System.out.printf("#%d %d\n", tc, D[N][N]);

        }
        System.out.println(( System.currentTimeMillis() - start )/1000.0 ); 
        sc.close();
    }
}





