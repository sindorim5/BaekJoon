package programmers.lv2;

import java.util.HashMap;

public class 모음사전 {
    int answer = 0;
    int count = 0;
    String[] alpha = {"A", "E", "I", "O", "U"};

    public int solution(String word) {
        dfs("", word);

        return answer;
    }

    public void dfs(String nowWord, String target) {
        if (nowWord.equals(target)) {
            answer = count;
            return;
        }

        if (nowWord.length() == 5) {
            return;
        }

        for(int i = 0; i < 5; i++) {
            count++;
            dfs(nowWord + alpha[i], target);
        }
    }

}
