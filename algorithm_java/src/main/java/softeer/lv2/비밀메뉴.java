package softeer.lv2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 비밀메뉴 {

    static int M, N, K;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        StringBuilder secret = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            secret.append(st.nextToken());
        }

        StringBuilder button = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            button.append(st.nextToken());
        }

        if (N < M) {
            System.out.println("normal");
        } else {
            if (button.toString().contains(secret.toString())) {
                System.out.println("secret");
            } else {
                System.out.println("normal");
            }
        }

    }

}
