package softeer.lv1;

import java.util.*;
import java.io.*;

public class 근무시간 {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int hour = 0;
        int minute = 0;

        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            String[] start = st.nextToken().split(":");
            String[] end = st.nextToken().split(":");

            int tempHour = Integer.parseInt(end[0]) - Integer.parseInt(start[0]);
            int tempMinute = Integer.parseInt(end[1]) - Integer.parseInt(start[1]);

            hour += tempHour;
            minute += tempMinute;

        }

        System.out.println(hour * 60 + minute);

    }


}
