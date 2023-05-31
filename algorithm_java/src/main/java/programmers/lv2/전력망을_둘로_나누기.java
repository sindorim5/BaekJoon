package programmers.lv2;

import java.util.*;
import java.util.stream.Collectors;

public class 전력망을_둘로_나누기 {
    int answer = Integer.MAX_VALUE;
    boolean[] connected;

    public int solution(int n, int[][] wires) {
        connected = new boolean[n];
        Arrays.fill(connected, true);

        for (int i = 0; i < n-1; i++) {
            connected[i] = false;
            bfs(wires[i][1], n, wires);
            connected[i] = true;
        }

        return answer;
    }

    public void bfs(int start, int n, int[][] wires) {
        LinkedList<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n + 1];
        int count = 1;
        queue.add(start);

        while (!queue.isEmpty()) {
            int now = queue.poll();
            visited[now] = true;

            for (int i = 0; i < wires.length; i++) {
                if (!connected[i]) continue;

                // int[] -> ArrayList<Integer>
                List <Integer> temp = Arrays.stream(wires[i]).boxed().collect(Collectors.toList());
                if (temp.contains(now)) {
                    for (int k = 0; k < temp.size(); k++) {
                        if (!visited[temp.get(k)] && !queue.contains(temp.get(k))) {
                            queue.add(temp.get(k));
                            count += 1;
                        }
                    }
                }
            }
        }

        answer = Math.min(Math.abs(count * 2 - n), answer);

    }
}
