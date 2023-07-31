package softeer.lv3;

import java.io.*;
import java.util.*;

public class 징검다리 {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] numbers = new int[N];
        int[] dp = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.fill(dp, 1);
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < i; j++) {
                if (numbers[j] < numbers[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int max = Integer.MIN_VALUE;
        for (int num : dp) {
            max = Math.max(num, max);
        }

        System.out.println(max);

    }
}
