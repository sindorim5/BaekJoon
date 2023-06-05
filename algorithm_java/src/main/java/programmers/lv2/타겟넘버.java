package programmers.lv2;

public class 타겟넘버 {
    int answer = 0;

    public int solution(int[] numbers, int target) {

        dfs(numbers, target, 0, 0);

        return answer;
    }

    public void dfs(int numbers[], int target, int index, int sum) {
        if (index == numbers.length) {
            if (sum == target) {
                answer += 1;
            }
            return;
        }

        dfs(numbers, target, index + 1, sum + numbers[index]);
        dfs(numbers, target, index + 1, sum - numbers[index]);

    }


}
