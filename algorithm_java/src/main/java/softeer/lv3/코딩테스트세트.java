package softeer.lv3;

import java.util.*;
import java.io.*;

public class 코딩테스트세트 {

    private static int N;
    private static long[] C, D;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());

        for (int i = 0; i < T; i++) {
            C = new long[N];
            D = new long[N];
            st = new StringTokenizer(br.readLine());
            long right = 0L;
            for (int j = 0; j < N - 1; j++) {
                C[j] = Long.parseLong(st.nextToken());
                D[j] = Long.parseLong(st.nextToken());
            }
            C[N - 1] = Long.parseLong(st.nextToken());

            System.out.println(bSearch(0, 2 * (long) Math.pow(10, 12)));
        }
    }

    public static boolean test(long testSets) {
        long[] S = new long[N];
        S[0] = C[0];
        for (int i = 0; i < N - 1; i++) {
            if (S[i] >= testSets) {
                S[i + 1] = C[i + 1] + D[i];
            } else if (S[i] + D[i] >= testSets) {
                S[i + 1] = C[i + 1] + (S[i] + D[i] - testSets);
            } else {
                return false;
            }
        }
        return S[N - 1] >= testSets;
    }

    public static long bSearch(long start, long end) {
        if (start == end) {
            return start;
        }
        long mid = (start + end + 1) / 2;
        if (test(mid)) {
            return bSearch(mid, end);
        } else {
            return bSearch(start, mid - 1);
        }
    }
}


/*
public class 코딩테스트세트 {
    public static int N,T;
    public static long arr[];

    public static void main(String[] args)throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        for(int i=0;i<T;i++){
            arr = new long[2*N-1];
            st = new StringTokenizer(br.readLine());
            long ans = 0;
            long left = 0;
            long right = 0;
            for(int j=0;j<2*N-1;j++){
                arr[j] = Long.parseLong(st.nextToken());
                if(j%2==1){
                    right = Math.max(right,Math.max(arr[j]+arr[j+1],arr[j]+arr[j-1]));
                }
            }
            while(left<=right){
                long mid = (left+right)/2;
                boolean flag = true;
                long diff = 0; // 2n에서 2n-1로 할당하고 남은 값 (초기 0)
                for(int j=1;j<2*N-1;j+=2){
                    long num = diff + arr[j-1]; // 2n번째 값
                    if(num<mid){
                        if(mid-num > arr[j]){ // 왼쪽에 할당해도 목표치보다 낮은 경우
                            flag = false;
                            break;
                        }else{
                            diff = arr[j] - (mid-num);// 왼쪽에 할당 후 갱신
                        }
                    }else{
                        diff = arr[j]; // 할당해줄 필요가 없는 경우
                    }
                }
                if(arr[2*N-2]+diff<mid){ // 마지막 원소 체크
                    flag = false;
                }
                if(flag){
                    left = mid+1;
                    ans = mid;
                }else{
                    right = mid-1;
                }
                System.out.println(Arrays.toString(arr));
            }
            System.out.println(ans);
        }
    }
}
 */