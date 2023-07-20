package softeer.lv2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class GBC {

    static class Node {
        int pos;
        int speed;

        public Node(int pos, int speed) {
            this.pos = pos;
            this.speed = speed;
        }

        @Override
        public String toString() {
            return "pos: " + this.pos + " spd: " + this.speed;
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        ArrayList<Node> areaList = new ArrayList<>();
        areaList.add(new Node(0, 0));
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int pos = Integer.parseInt(st.nextToken());
            int speed = Integer.parseInt(st.nextToken());

            Node node = areaList.get(i - 1);
            areaList.add(new Node(node.pos + pos, speed));
        }

        ArrayList<Node> testList = new ArrayList<>();
        testList.add(new Node(0, 0));
        for (int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine());
            int pos = Integer.parseInt(st.nextToken());
            int speed = Integer.parseInt(st.nextToken());

            Node node = testList.get(i - 1);
            testList.add(new Node(node.pos + pos, speed));
        }

        PriorityQueue<Integer> queue = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });

        int areaIndex = 1;
        int index = 1;
        while (index < testList.size()) {
            if (areaIndex == areaList.size()) {
                areaIndex -= 1;
            }
            Node areaNode = areaList.get(areaIndex);
            Node testNode = testList.get(index);
            if (areaNode.pos < testNode.pos) {
                areaIndex += 1;
            } else if (areaNode.pos > testNode.pos) {
                index += 1;
            } else {
                index += 1;
                areaIndex += 1;
            }
            queue.add(Math.max(testNode.speed - areaNode.speed, 0));
        }
        System.out.println(queue.poll());
    }

}
