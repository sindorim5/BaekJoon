package programmers.lv1;

import java.util.Arrays;

public class 최소직사각형 {

    public int solution(int[][] sizes) {
        int maxWidth = 0;
        int maxHeight = 0;

        for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] < sizes[i][1]) {
                int temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
            }
            if (sizes[i][0] > maxWidth) {
                maxWidth = sizes[i][0];
            }
            if (sizes[i][1] > maxHeight) {
                maxHeight = sizes[i][1];
            }
        }

        return maxWidth * maxHeight;
    }

}
