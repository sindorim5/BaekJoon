package softeer.lv2;

import java.util.*;
import java.io.*;


public class 전광판 {
    static int[] zero = {1, 1, 1, 1, 1, 1, 0};
    static int[] one = {0, 1, 1, 0, 0, 0, 0};
    static int[] two = {1, 1, 0, 1, 1, 0, 1};
    static int[] three = {1, 1, 1, 1, 0, 0, 1};
    static int[] four = {0, 1, 1, 0, 0, 1, 1};
    static int[] five = {1, 0, 1, 1, 0, 1, 1};
    static int[] six = {1, 0, 1, 1, 1, 1, 1};
    static int[] seven = {1, 1, 1, 0, 0, 1, 0};
    static int[] eight = {1, 1, 1, 1, 1, 1, 1};
    static int[] nine = {1, 1, 1, 1, 0, 1, 1};
    static ArrayList<int[]> digital = new ArrayList<>() {{
        add(zero);
        add(one);
        add(two);
        add(three);
        add(four);
        add(five);
        add(six);
        add(seven);
        add(eight);
        add(nine);
    }};
    static Map<String, int[]> digits = new TreeMap<>();


    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i <= 9; i++) {
            String s = Integer.toString(i);
            digits.put(s, digital.get(i));
        }

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String[] a = st.nextToken().split("");
            String[] b = st.nextToken().split("");

            int result = 0;
            if (a.length > b.length) {
                result = calculate(a, b);
            } else if (b.length > a.length) {
                result = calculate(b, a);
            } else {
                result = calculate(a, b);
            }

            System.out.println(result);

        }
    }

    static int calculate(String[] a, String[] b) {
        int aLength = a.length;
        int bLength = b.length;

        int count = 0;
        if (aLength == bLength) {
            aLength -= 1;
            while (aLength >= 0) {
                int[] aDigits = digits.get(a[aLength]);
                int[] bDigits = digits.get(b[aLength]);

                for (int i = 0; i < 7; i++) {
                    if (aDigits[i] != bDigits[i]) {
                        count += 1;
                    }
                }
                aLength -= 1;
            }
        } else if (aLength > bLength) {
            aLength -= 1;
            bLength -= 1;
            while (bLength >= 0) {
                int[] aDigits = digits.get(a[aLength]);
                int[] bDigits = digits.get(b[bLength]);

                for (int i = 0; i < 7; i++) {
                    if (aDigits[i] != bDigits[i]) {
                        count += 1;
                    }
                }
                aLength -= 1;
                bLength -= 1;
            }

            while (aLength >= 0) {
                int[] aDigits = digits.get(a[aLength]);

                for (int i = 0; i < 7; i++) {
                    if (aDigits[i] == 1) {
                        count += 1;
                    }
                }
                aLength -= 1;
            }
        }

        return count;
    }
}