package softeer.lv3;

import java.io.*;
import java.util.*;

public class 징검다리_이분탐색 {

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer>LIS = new ArrayList<>();
        LIS.add(numbers[0]);

        for (int i = 1; i < N; i++) {
            int value = numbers[i];

            if (value > LIS.get(LIS.size() - 1)) {
                LIS.add(value);
            } else {
                int pos = -Collections.binarySearch(LIS, value) - 1;
                LIS.set(pos, value);
            }
        }

        System.out.println(LIS.size());
    }
}
