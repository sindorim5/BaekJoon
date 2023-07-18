package softeer.lv2;

import java.util.*;
import java.io.*;


public class 장애물인식프로그램 {

    static class Point {
        int y;
        int x;

        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static int N;

    static int[] dY = {0, 1, 0, -1};
    static int[] dX = {1, 0, -1, 0};

    static int[][] matrix;
    static boolean[][] visited;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        matrix = new int[N][N];
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            String[] inputs = br.readLine().split("");
            for (int j = 0; j < N; j++) {
                matrix[i][j] = Integer.parseInt(inputs[j]);
            }
        }

        ArrayList<Integer> blocks = new ArrayList<>();
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                if (matrix[y][x] == 1 && !visited[y][x]) {
                    int block = bfs(y, x);
                    blocks.add(block);
                }
            }
        }

        blocks.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1 - o2;
            }
        });
        System.out.println(blocks.size());
        for (int block : blocks) {
            System.out.println(block);
        }
    }

    static int bfs(int y, int x) {
        int count = 1;
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(y, x));
        visited[y][x] = true;

        while (!queue.isEmpty()) {
            Point point = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nY = point.y + dY[i];
                int nX = point.x + dX[i];
                if (nY < 0) continue;
                if (nY >= N) continue;
                if (nX < 0) continue;
                if (nX >= N) continue;

                if (matrix[nY][nX] == 1 && !visited[nY][nX]) {
                    Point temp = new Point(nY, nX);
                    visited[nY][nX] = true;
                    count += 1;
                    queue.add(temp);

                }
            }

        }

        return count;

    }
}