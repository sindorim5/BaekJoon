package programmers.lv2;

public class 피로도 {
    int answer = -1;
    boolean[] visited;
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];

        dfs(0, k, dungeons);

        return answer;
    }

    public void dfs(int depth, int fatigability, int[][] dungeons) {

        if (depth > answer) answer = depth;

        for (int i = 0; i < dungeons.length; i++) {
            if (visited[i]) continue;

            if (fatigability >= dungeons[i][0]) {
                visited[i] = true;
                dfs(depth + 1, fatigability - dungeons[i][1], dungeons);
                visited[i] = false;
            }
        }
    }

}