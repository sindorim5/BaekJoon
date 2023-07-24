package softeer.lv3;


import java.util.*;
import java.io.*;

public class 수퍼바이러스 {
    static long K, P, N;

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        K = Long.parseLong(st.nextToken());
        P = Long.parseLong(st.nextToken());
        N = Long.parseLong(st.nextToken());

        long result = dfs(P, 10 * N);

        System.out.println(K * result % 1000000007);
    }

    static long dfs(long p, long n) {
        if (n == 1) {
            return p;
        }

        long temp = 0L;

        if (n % 2 == 0) {
            temp = dfs(p, n / 2);
            return temp * temp % 1000000007;
        } else {
            temp = dfs(p, (n - 1) / 2);
            return (temp * temp % 1000000007) * p % 1000000007;
        }
    }

}

/*
3^10 = 3^5 * 3^5 = (3^2 * 3^2 * 3) ^ 2
 */