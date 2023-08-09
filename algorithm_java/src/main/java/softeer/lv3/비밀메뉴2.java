package softeer.lv3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 비밀메뉴2 {

    static int N, M, K;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        int[] dpA = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            dpA[i] = Integer.parseInt(st.nextToken());
        }

        int[] dpB = new int[M + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= M; i++) {
            dpB[i] = Integer.parseInt(st.nextToken());
        }

//        System.out.println(Arrays.toString(dpA));
//        System.out.println(Arrays.toString(dpB));
//        System.out.println("#########################");


        int[][] dp = new int[N + 1][M + 1];
        int maxValue = 0;
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                if (dpA[i] == dpB[j]) {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j - 1] + 1);
                } else {
                    dp[i][j] = dp[i][j - 1];
                }
            }
        }

        System.out.println(dp[N][M]);


    }
}
