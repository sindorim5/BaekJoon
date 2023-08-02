package softeer.lv3;

import java.io.*;
import java.util.*;

public class 강의실배정 {

    static class Lecture implements Comparable {
        int start;
        int end;

        public Lecture(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Object o) {
            Lecture l = (Lecture) o;

            if (this.end == l.end) {
                return this.start - l.start;
            }
            return this.end - l.end;
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)", this.start, this.end);
        }
    }


    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        List<Lecture> lectureList = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            lectureList.add(new Lecture(start, end));
        }

        Collections.sort(lectureList);

        for (Lecture l : lectureList) {
            System.out.println(l.toString());
        }

        int count = 0;
        int endTime = 0;
        for (Lecture l : lectureList) {
            if (endTime <= l.start) {
                count += 1;
                endTime = l.end;
            }
        }

        System.out.println(count);


    }
}
