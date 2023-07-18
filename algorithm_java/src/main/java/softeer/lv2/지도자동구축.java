package softeer.lv2;

import java.util.*;
import java.io.*;


public class 지도자동구축 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[N + 1];

        dp[0] = 2;
        for (int i = 1; i <= N; i++) {
            dp[i] = dp[i - 1] + dp[i - 1] - 1;
        }
        System.out.println(dp[N] * dp[N]);
    }

}