package baekjoon.gold.three;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 앱 {

    static class App {
        int memory;
        int cost;

        public App(int memory, int cost) {
            this.memory = memory;
            this.cost = cost;
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)", this.memory, this.cost);
        }
    }

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N, M;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());   // 확보해야 하는 메모리

        StringTokenizer memoryTokenizer = new StringTokenizer(br.readLine());
        StringTokenizer costTokenizer = new StringTokenizer(br.readLine());

        ArrayList<App> appList = new ArrayList<>();
        appList.add(new App(0, 0));

        int totalCost = 0;
        for (int i = 0; i < N; i++) {
            int memory = Integer.parseInt(memoryTokenizer.nextToken());
            int cost = Integer.parseInt(costTokenizer.nextToken());

            totalCost += cost;
            appList.add(new App(memory, cost));
        }

        int[][] dp = new int[N + 1][10001];
        for (int i = 1; i <= N; i++) {
            App app = appList.get(i);

            for (int cost = 0; cost <= 10000; cost++) {
                if (cost >= app.cost) {
                    dp[i][cost] = Math.max(app.memory, dp[i - 1][cost - app.cost] + app.memory);
                } else {
                    dp[i][cost] = dp[i - 1][cost];
                }
            }
        }

        for (int i = 0; i <= 10000; i++) {
            if (dp[N][i] >= M) {
                System.out.println(i);
                break;
            }
        }

    }

}

/*
19 20169
240 2560 434 6 31 577 500 2715 2916 952 2490 258 1983 1576 3460 933 1660 2804 2584
82 77 81 0 36 6 53 78 49 82 82 33 66 8 60 0 98 91 93

7 120
20 91 92 93 94 95 100
1 2 2 2 2 2 2
-> 3
 */