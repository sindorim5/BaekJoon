package programmers.lv2;

import java.util.HashSet;

public class 소수찾기 {
    HashSet<Integer> hashSet = new HashSet<>();
    char[] numberList;
    boolean[] visited;

    public int solution(String numbers) {
        int answer = 0;
        numberList = new char[numbers.length()];
        visited = new boolean[numbers.length()];

        for (int i = 0; i < numbers.length(); i++) {
            numberList[i] = numbers.charAt(i);
        }

        dfs("", 0);

        answer = hashSet.size();

        return answer;
    }

    public void dfs(String numberString, int index) {
        int number;
        if (!numberString.equals("")) {
            number = Integer.parseInt(numberString);
            if (isPrimeNumber(number)) {
                hashSet.add(number);
            }
        }
        if (index == numberList.length) return;

        for (int i = 0; i < numberList.length; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            dfs(numberString + numberList[i], index + 1);
            visited[i] = false;
        }
    }

    public boolean isPrimeNumber(int number) {
        if (number == 0 || number == 1) {
            return false;
        }

        int rootValue = (int) Math.sqrt(number);

        for (int i = 2; i <= rootValue; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }

}
