package programmers.lv2;

import java.util.LinkedList;
import java.util.Queue;

public class 게임_맵_최단거리 {

    static class Point {
        int y,x;

        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public int solution(int[][] maps) {
        int answer = 0;
        // 하 우 상 좌
        int[] dY = new int[]{1, 0, -1, 0};
        int[] dX = new int[]{0, 1, 0, -1};
        Queue<Point> queue = new LinkedList<>();
        int[][] depthMap = new int[maps.length][maps[0].length];

        queue.add(new Point(0, 0));
        depthMap[0][0] = 1;

        while(!queue.isEmpty()) {
            Point point = queue.poll();
            int depth = depthMap[point.y][point.x];

            for (int i = 0; i < 4; i++) {
                int nY = point.y + dY[i];
                int nX = point.x + dX[i];

                // 맵 밖으로 나갈 경우
                if (nY < 0 || nX < 0 || nY >= maps.length || nX >= maps[0].length) {
                    continue;
                }
                // 벽인 경우
                if (maps[nY][nX] == 0) {
                    continue;
                }

                // depth + 1 해서 찍어주고 벽으로 막기
                depthMap[nY][nX] = depth + 1;
                maps[nY][nX] = 0;

                queue.add(new Point(nY, nX));
            }
        }

        answer = depthMap[maps.length-1][maps[0].length - 1];

        if (answer == 0) {
            answer = -1;
        }

        return answer;
    }
}

/*
    DFS는 효율성 통과를 못함
    // 하 우 상 좌
    int[] dY = new int[]{1, 0, -1, 0};
    int[] dX = new int[]{0, 1, 0, -1};
    int length = Integer.MAX_VALUE;

    public int solution(int[][] maps) {
        int answer = 0;
        boolean[][] visited = new boolean[maps.length][maps[0].length];

        dfs(0,0, 0, visited, maps);

        if (length == Integer.MAX_VALUE) {
            answer = -1;
        } else {
            answer = length;
        }

        return answer;
    }

    public void dfs(int y, int x, int depth, boolean[][] visited, int[][] maps) {
        depth += 1;

        if (depth >= length) {
            return;
        }

        if ((y == maps.length - 1) && (x == maps[0].length - 1)) {
            length = depth;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nY = y + dY[i];
            int nX = x + dX[i];

            // maps 안에 있는가
            if (nY < 0 || nX < 0 || nY >= maps.length || nX >= maps[0].length) {
                continue;
            }

            if (!visited[nY][nX] && maps[nY][nX] == 1) {
                visited[y][x] = true;
                dfs(nY, nX, depth, visited, maps);
                visited[y][x] = false;
            }
        }
    }
 */