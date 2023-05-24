package programmers.lv1;

import java.util.ArrayList;
import java.util.Arrays;

public class 모의고사 {

    int[] supo1 = {1, 2, 3, 4, 5};
    int[] supo2 = {2, 1, 2, 3, 2, 4, 2, 5};
    int[] supo3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

    int size1 = supo1.length;
    int size2 = supo2.length;
    int size3 = supo3.length;

    public int[] solution(int[] answers) {
        int[] answer = {};
        ArrayList<Integer> answerList = new ArrayList<>();
        int[] count = {0, 0, 0};

        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == supo1[i % size1]) {
                count[0] += 1;
            }
            if (answers[i] == supo2[i % size2]) {
                count[1] += 1;
            }
            if (answers[i] == supo3[i % size3]) {
                count[2] += 1;
            }
        }

        int maxValue = Arrays.stream(count).max().getAsInt();

        for (int i = 0; i < count.length; i++) {
            if (maxValue == count[i]) {
                answerList.add(i + 1);
            }
        }

        answer = answerList.stream().mapToInt(i -> i).toArray();


        return answer;
    }
}
