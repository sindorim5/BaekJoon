package baekjoon.gold.one;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 구간합구하기 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N, M, K;
    static long[] numbers;
    static long[] tree;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        numbers = new long[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Long.parseLong(br.readLine());
        }
        tree = new long[N * 4];

        initTree(0, N - 1, 1);

        for (int i = 0; i < M + K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            if (a == 1) {
                long diff = c - numbers[b - 1];
                numbers[b - 1] = c;
                update(0, N - 1, 1, b - 1, diff);
            } else {
                System.out.println(sum(0, N - 1, 1, b - 1, (int) c - 1));
            }

        }


    }

    static long initTree(int start, int end, int node) {
        if (start == end) {
            return tree[node] = numbers[start];
        }

        int mid = (start + end) / 2;

        return tree[node] = initTree(start, mid, node * 2) + initTree(mid + 1, end, node * 2 + 1);
    }

    static void update(int start, int end, int node, int index, long value) {

        // 범위 밖이면 상관 없다
        if (index < start || index > end) {
            return;
        }

        // 범위 안이라면 부분 합을 업데이트
        tree[node] += value;

        // 리프 노드라면 더 탐색할 필요가 없다
        if (start == end) {
            return;
        }

        int mid = (start + end) / 2;
        // 왼쪽, 오른쪽 노드에 대해서도 수행
        update(start, mid, node * 2, index, value);
        update(mid + 1, end, node * 2 + 1, index, value);
    }

    static long sum(int start, int end, int node, int left, int right) {

        // 범위 밖
        if (left > end || right < start) {
            return 0;
        }

        // 범위 안
        if (left <= start && end <= right) {
            return tree[node];
        }

        // 찾지 못했으면 쪼개서 탐색
        int mid = (start + end) / 2;
        return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right);

    }

}
