package softeer.lv2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 금고털이 {

    static class Metal implements Comparable<Metal> {
        int weight;
        int value;

        public Metal(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }

        @Override
        public int compareTo(Metal metal) {
            return metal.value - this.value;
        }

    }

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int W, N;

    public static void main(String args[]) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        ArrayList<Metal> metalList = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int weight = Integer.parseInt(st.nextToken());
            int value = Integer.parseInt(st.nextToken());
            metalList.add(new Metal(weight, value));
        }

        metalList.sort(Metal::compareTo);

        int index = 0;
        int resultValue = 0;
        while (W > 0) {

            if (index == metalList.size()) {
                break;
            }

            Metal temp = metalList.get(index);

            if (W >= temp.weight) {
                W -= temp.weight;
                resultValue += temp.value * temp.weight;
            } else {
                resultValue += temp.value * W;
                W -= W;
            }
            index++;
        }

        System.out.println(resultValue);
    }

}
