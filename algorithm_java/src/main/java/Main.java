import programmers.lv3.베스트앨범;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        베스트앨범 BestAlbum = new 베스트앨범();

        int[] sol = BestAlbum.solution(
                new String[]{"classic", "pop", "classic", "classic", "pop"},
                new int[]{500, 600, 150, 800, 2500}
        );
        System.out.println(Arrays.toString(sol));
    }

}
