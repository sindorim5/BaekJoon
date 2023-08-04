package softeer.lv3;

import java.util.*;
import java.io.*;


// fail
public class 거리합구하기
{
    static class Node implements Comparable<Node> {
        int end;
        long distance;

        public Node(int end, long distance) {
            this.end = end;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            if (this.distance > o.distance) {
                return 1;
            } else if (this.distance == o.distance) {
                return 0;
            } else {
                return -1;
            }
        }

    }

    static long[][] matrix;
    static ArrayList<ArrayList<Node>> nodeList;


    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        matrix = new long[N+1][N+1];
        nodeList = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            nodeList.add(new ArrayList<Node>());
        }

        StringTokenizer st;
        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            long dist = Long.parseLong(st.nextToken());

            nodeList.get(start).add(new Node(end, dist));
            nodeList.get(end).add(new Node(start, dist));
        }

        for (int i = 1; i <= N; i++) {
            dijkstra(i);
        }

        for (int i = 1; i <= N; i++) {
            long sum = 0;
            for (int j = 1; j <= N; j++) {
                sum += matrix[i][j];
            }
            System.out.println(sum);
        }

    }

    static void dijkstra(int start) {
        Arrays.fill(matrix[start], Long.MAX_VALUE);
        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.add(new Node(start, 0));

        matrix[start][start] = 0;

        while (!queue.isEmpty()) {
            Node now = queue.poll();

            ArrayList<Node> nodes = nodeList.get(now.end);

            for (Node node : nodes) {
                if (matrix[start][node.end] > matrix[start][now.end] + node.distance) {
                    matrix[start][node.end] = matrix[start][now.end] + node.distance;
                    queue.add(new Node(node.end, matrix[start][node.end]));
                }
            }
        }
    };

}