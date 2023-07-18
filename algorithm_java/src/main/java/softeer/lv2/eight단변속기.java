package softeer.lv2;

import java.util.*;
import java.io.*;


public class eight단변속기 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inputText = br.readLine();

        String ascend = "1 2 3 4 5 6 7 8";
        String descend = "8 7 6 5 4 3 2 1";

        if (ascend.equals(inputText)) {
            System.out.println("ascending");
        } else if (descend.equals(inputText)) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }

    }
}
