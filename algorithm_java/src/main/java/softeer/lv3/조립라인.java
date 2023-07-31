package softeer.lv3;

import java.util.*;
import java.io.*;


public class 조립라인 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        if (N == 1) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            System.out.println(Math.min(A, B));
        } else {
            int[] A = new int[N + 1];
            int[] B = new int[N + 1];
            int[] moveToB = new int[N + 1];
            int[] moveToA = new int[N + 1];
            for (int i = 1; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                A[i] = Integer.parseInt(st.nextToken());
                B[i] = Integer.parseInt(st.nextToken());
                moveToB[i + 1] = Integer.parseInt(st.nextToken());
                moveToA[i + 1] = Integer.parseInt(st.nextToken());
            }

            StringTokenizer st = new StringTokenizer(br.readLine());
            A[N] = Integer.parseInt(st.nextToken());
            B[N] = Integer.parseInt(st.nextToken());

            int a = 0;
            int b = 1;
            // N회차마다 a라인 b라인의 최솟값을 저장하는 dp
            int[][] dp = new int[N + 1][2];

            for (int i = 1; i <= N; i++) {
                // A라인으로 계속 가는 경우 vs B에서 A로 이동해 오는 경우
                dp[i][a] = Math.min(
                        dp[i - 1][a] + A[i],
                        dp[i - 1][b] + moveToA[i] + A[i]
                );
                // B라인으로 계속 가는 경우 vs A에서 B로 이동해 오는 경우
                dp[i][b] = Math.min(
                        dp[i - 1][b] + B[i],
                        dp[i - 1][a] + moveToB[i] + B[i]
                );
            }
            System.out.println(Math.min(dp[N][a], dp[N][b]));
        }
    }
}