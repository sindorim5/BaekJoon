package programmers.lv1;

import java.util.*;

public class 개인정보_수집_유효기간 {
    public int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<String, Integer> termMap = new HashMap<>();

        int todayInt = getDate(today);

        for (String term : terms) {
            String[] sTerm = term.split(" ");
            termMap.put(sTerm[0], Integer.parseInt(sTerm[1]) * 28);
        }

        for (int i = 0; i < privacies.length; i++) {
            String privacy = privacies[i];
            String[] sPrivacy = privacy.split(" ");
            int dayInt = getDate(sPrivacy[0]);
            int valid = termMap.get(sPrivacy[1]);
            int diff = todayInt - dayInt;

            if (diff >= valid) {
                answer.add(i + 1);
            }

        }


        return answer.stream().mapToInt(Integer -> Integer).toArray();
    }

    public int getDate(String today) {
        String[] sToday = today.split("\\.");
        int year = Integer.parseInt(sToday[0]);
        int month = Integer.parseInt(sToday[1]);
        int day = Integer.parseInt(sToday[2]);

        return year * 12 * 28 + month * 28 + day;
    }
}
