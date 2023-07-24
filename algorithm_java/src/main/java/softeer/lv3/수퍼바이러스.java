package softeer.lv3;


import java.util.*;
import java.io.*;

public class 수퍼바이러스 {
    static double K, P, N;

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        K = Double.parseDouble(st.nextToken());
        P = Double.parseDouble(st.nextToken());
        N = Double.parseDouble(st.nextToken());

        double result = dfs(P, 10 * N);

        System.out.println(String.format("%.0f", K * result % 1000000007));
    }

    static double dfs(double p, double n) {
        if (n == 1.0) {
            return p;
        }

        double temp = 0.0;

        if (n % 2 == 0.0) {
            temp = dfs(p, n / 2);
            return temp * temp % 1000000007;
        } else {
            temp = dfs(p, (n - 1) / 2);
            return temp * temp * p % 1000000007;
        }
    }

}