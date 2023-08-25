package softeer.lv3;

import java.util.*;
import java.io.*;


public class 자동차테스트 {
    static int N, Q;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        ArrayList<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            numbers.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(numbers);
        for (int q = 0; q < Q; q++) {
            int num = Integer.parseInt(br.readLine());

            int index = Collections.binarySearch(numbers, num);

            if (index < 0) {
                System.out.println(0);
            } else {
                int right = numbers.size() - index - 1;

                System.out.println(index * right);
            }

        }

    }
}