package programmers.lv3;

public class 네트워크 {
    boolean[] visited;

    public int solution(int n, int[][] computers) {
        int answer = 0;

        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, n, computers);
                answer += 1;
            }
        }

        return answer;
    }

    public void dfs(int index, int n, int[][] computers) {
        visited[index] = true;

        for (int i = 0; i < n; i++) {
            if (computers[index][i] == 1 && !visited[i]) {
                dfs(i, n, computers);
            }
        }
    }

}
