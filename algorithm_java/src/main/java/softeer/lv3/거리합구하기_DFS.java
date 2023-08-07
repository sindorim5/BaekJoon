package softeer.lv3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 거리합구하기_DFS {
    static class Node {
        int end;
        long distance;

        public Node(int end, long distance) {
            this.end = end;
            this.distance = distance;
        }

    }

    static int N;
    static ArrayList<ArrayList<Node>> nodeList;
    static int[] subtreeSize;
    static long[] distances;
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        nodeList = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            nodeList.add(new ArrayList<>());
        }

        for (int i = 0; i < N-1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            nodeList.get(a).add(new Node(b, d));
            nodeList.get(b).add(new Node(a, d));

        }

        subtreeSize = new int[N+1];
        distances = new long[N+1];

        dfs1(1, 1);
        dfs2(1, 1);

        for (int i = 1; i <= N; i++) {
            System.out.println(distances[i]);
        }

    }

    static void dfs1(int current, int parent) {
        subtreeSize[current] = 1;
        for (int i = 0; i < nodeList.get(current).size(); i++) {
            Node node = nodeList.get(current).get(i);

            if (node.end != parent) {
                dfs1(node.end, current);
                distances[current] += subtreeSize[node.end] * node.distance + distances[node.end];
                subtreeSize[current] += subtreeSize[node.end];
            }
        }
    }

    static void dfs2(int current, int parent) {
        for (int i = 0; i < nodeList.get(current).size(); i++) {
            Node node = nodeList.get(current).get(i);

            if (node.end != parent) {
                distances[node.end] = distances[current] + node.distance * (N - subtreeSize[node.end] * 2L);
                dfs2(node.end, current);
            }
        }
    }

}

/*
1번 노드를 기준으로는 똑같이 계산한다
1과 인접한 노드에 대해서는 상수 시간에 구한다
이를 위해 subtree size가 필요하다
subtree size란 ? 어떤 노드를 root로 했을 때, 본인을 포함한 노드 개수는 ?

2번 노드를 기준으로 생각했을 때,
나머지 6개 노드에 대해서 1번을 거쳐서 2번으로 들어오므로, D(1,2) = 5 만큼 증가한다
2의 subtree들은 5가 감소한다
 */