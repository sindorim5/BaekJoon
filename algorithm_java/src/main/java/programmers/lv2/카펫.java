package programmers.lv2;

import java.util.Arrays;

public class 카펫 {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};

        int a = brown + yellow; // x * y
        int b = (brown + 4) / 2; // x + y

        for (int x = a; x > 0; x--) {
            if (a % x == 0) {
                int y = a / x;
                if (x + y == b) {
                    answer = new int[]{x, y};
                    break;
                }
            }
        }

        return answer;
    }
}