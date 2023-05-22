package programmers.lv3;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;

public class 베스트앨범 {
    static class Music {
        String genre;
        int play;
        int index;

        public Music(String genre, int play, int index) {
            this.genre = genre;
            this.play = play;
            this.index = index;
        }
    }

    public int[] solution(String[] genres, int[] plays) {

        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < genres.length; i++) {
            map.put(genres[i], map.getOrDefault(genres[i], 0) + plays[i]);
        }

        ArrayList<String> genres_ordered = new ArrayList<String>();
        while (map.size() != 0) {
            int max = -1;
            String max_key = "";
            for (String key : map.keySet()) {
                int tmp_cnt = map.get(key);
                if (tmp_cnt > max) {
                    max = tmp_cnt;
                    max_key = key;
                }
            }
            genres_ordered.add(max_key);
            map.remove(max_key);
        }

        ArrayList<Music> result = new ArrayList<>();
        for (String genre : genres_ordered) {
            ArrayList<Music> musicList = new ArrayList<>();
            for (int i = 0; i < genres.length; i++) {
                if (genres[i].equals(genre)) {
                    musicList.add(new Music(genre, plays[i], i));
                }
            }
            musicList.sort((o1, o2) -> o2.play - o1.play);
            result.add(musicList.get(0));
            if (musicList.size() != 1) {
                result.add(musicList.get(1));
            }
        }

        System.out.println(result);

        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i).index;
        }
        return answer;
    }
}
