package softeer.lv3;

import java.io.*;
import java.util.*;

public class 순서대로방문하기 {
    static int[][] d = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    static int N, M;
    static int[][] matrix;
    static boolean[][] visited;
    static List<int[]> checkPoints = new ArrayList<>();
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);

        matrix = new int[N][N];
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            input = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                matrix[i][j] = Integer.parseInt(input[j]);
            }
        }

        for (int i = 0; i < M; i++) {
            input = br.readLine().split(" ");
            int y = Integer.parseInt(input[0]) - 1;
            int x = Integer.parseInt(input[1]) - 1;
            checkPoints.add(new int[]{y, x});
        }

        visited[checkPoints.get(0)[0]][checkPoints.get(0)[1]] = true;
        dfs(checkPoints.get(0)[0], checkPoints.get(0)[1], 0);

        System.out.println(result);
    }

    static void dfs(int y, int x, int depth) {
        // 모든 체크포인트에 도달해다면 result에 추가
        if (depth == M) {
            result += 1;
            return;
        }

        // 지금 도착한 장소가 체크포인트라면 (depth + 1)
        if (y == checkPoints.get(depth)[0] && x == checkPoints.get(depth)[1]) {
            dfs(y, x, depth + 1);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nY = y + d[i][0];
            int nX = x + d[i][1];

            // matrix 밖으로 나가면 continue
            if (nY < 0 || nX < 0 || nY >= N || nX >= N) continue;

            // 1로 된 부분은 못 가니까 continue
            if (matrix[nY][nX] == 1) continue;

            // 이미 왔다간 경로이면 continue
            if (visited[nY][nX]) continue;

            visited[nY][nX] = true;
            dfs(nY, nX, depth);
            visited[nY][nX] = false;
        }
    }
}

