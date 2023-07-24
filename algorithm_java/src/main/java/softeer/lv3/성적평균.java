package softeer.lv3;

import java.util.*;
import java.io.*;


public class 성적평균
{
    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] numbers = new int[N+1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            numbers[i] = numbers[i-1] + Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            double sum = numbers[b] - numbers[a - 1];
            double div = b - a + 1;

            double result = Math.round(sum * 100.0 / div) / 100.0;

            System.out.println(String.format("%.2f", result));
        }

    }
}