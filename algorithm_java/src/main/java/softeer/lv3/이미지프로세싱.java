package softeer.lv3;

import java.util.*;
import java.io.*;

public class 이미지프로세싱
{
    static int H,W,Q;
    static int[] dY = {1, 0, -1, 0};
    static int[] dX = {0, 1, 0, -1};
    static int[][] matrix;
    static boolean[][] visited;

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());

        matrix = new int[H][W];
        for (int i = 0; i < H; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < W; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Q = Integer.parseInt(br.readLine());
        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken()) - 1;
            int j = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken());
            visited = new boolean[H][W];
            bfs(i, j, c);
        }

        for (int y = 0; y < H; y++) {
            for (int x = 0; x < W; x++) {
                System.out.print(matrix[y][x] + " ");
            }
            System.out.print("\n");
        }
    }

    static void bfs(int i, int j, int c) {
        int original = matrix[i][j];
        if (original == c) {
            return;
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(i * W + j);
        visited[i][j] = true;

        while (!queue.isEmpty()) {
            int p = queue.poll();
            int y = p / W;
            int x = p % W;

            matrix[y][x] = c;

            for (int idx = 0; idx < 4; idx++) {
                int nY = y + dY[idx];
                int nX = x + dX[idx];

                if (nY < 0 || nX < 0 || nY >= H || nX >= W) continue;
                if (matrix[nY][nX] != original || visited[nY][nX]) continue;

                queue.offer(nY * W + nX);
                visited[nY][nX] = true;
            }
        }

    }
}