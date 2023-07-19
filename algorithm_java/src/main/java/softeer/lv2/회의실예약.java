package softeer.lv2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 회의실예약 {

    static class Time {
        int start;
        int end;

        public Time(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }


    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, ArrayList<Time>> reservation = new TreeMap<>();
        Map<String, ArrayList<Time>> available = new TreeMap<>();
        for (int i = 0; i < N; i++) {
            String room = br.readLine();
            reservation.put(room, new ArrayList<>());
            available.put(room, new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            String[] input = br.readLine().split(" ");
            reservation.get(input[0]).add(
                    new Time(Integer.parseInt(input[1]), Integer.parseInt(input[2]))
            );
        }

        for (String key : reservation.keySet()) {
            int end = 9;

            reservation.get(key).sort(new Comparator<Time>() {
                @Override
                public int compare(Time time, Time t1) {
                    return time.start - t1.start;
                }
            });

            for (Time time : reservation.get(key)) {
                if (time.start > end) {
                    available.get(key).add(
                            new Time(end, time.start)
                    );
                    end = time.end;
                }
                else if (time.start == end) {
                    end = time.end;
                }
            }
            if (end < 18) {
                available.get(key).add(new Time(end , 18));
            }
        }

        int index = 0;
        for (String key : available.keySet()) {
            System.out.println("Room " + key + ":");
            ArrayList<Time> times = available.get(key);
            if (times.size() == 0) {
                System.out.println("Not available");
            } else {
                System.out.println(times.size() + " available:");
            }

            for (Time time : times) {
                System.out.printf("%02d-%02d%n", time.start, time.end);
            }

            index += 1;
            if (index != N) {
                System.out.println("-----");
            }
        }
    }


}
