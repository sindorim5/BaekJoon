package softeer.lv2;

import java.util.*;
import java.io.*;

public class 바이러스 {

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long K = Long.parseLong(st.nextToken());
        long P = Long.parseLong(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        long result = K;
        for (int i = 0; i < N; i++) {
            result = result * P % 1000000007;
        }

        System.out.println(result);

    }

}
