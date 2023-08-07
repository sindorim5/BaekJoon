package softeer.lv3;

import java.util.*;
import java.io.*;

public class 좌석관리 {

    static class Employee {
        public int x, y;
        public boolean ate;

        public Employee(int x, int y, boolean ate) {
            this.x = x;
            this.y = y;
            this.ate = ate;
        }
    }


    static int[][] matrix;
    static Map<Integer, Employee> employees = new HashMap<>();
    static int N, M, Q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        matrix = new int[N][M];

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            String action = st.nextToken();
            int id = Integer.parseInt(st.nextToken());

            if (action.equals("Out")) {
                if (!employees.containsKey(id)) {
                    System.out.println(id + " didn't eat lunch.");
                } else {
                    Employee emp = employees.get(id);
                    if (emp.ate) {
                        System.out.println(id + " already left seat.");
                    } else {
                        System.out.println(id + " leaves from the seat (" + (emp.x + 1) + ", " + (emp.y + 1) + ").");
                        emp.ate = true;
                        matrix[emp.x][emp.y] = 0;
                        checkAvailable(emp.x, emp.y, 1);
                    }
                }
            } else {
                if (!employees.containsKey(id)) {
                    System.out.println(searchSeat(id));
                } else {
                    Employee emp = employees.get(id);
                    if (emp.ate) {
                        System.out.println(id + " already ate lunch.");
                    } else {
                        System.out.println(id + " already seated.");
                    }
                }
            }
        }
    }

    public static void checkAvailable(int x, int y, int id) {
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        for (int[] dir : directions) {
            int nx = x + dir[0];
            int ny = y + dir[1];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                matrix[nx][ny] += id;
            }
        }
    }

    public static String searchSeat(int id) {
        int tx = 0, ty = 0;
        double minDistance = 0;

        for (int x = 0; x < N; x++) {
            for (int y = 0; y < M; y++) {
                if (matrix[x][y] == 0) {
                    double tempMin = Integer.MAX_VALUE;
                    for (Employee emp : employees.values()) {
                        if (emp.ate) continue;
                        double d = Math.sqrt(Math.pow(emp.x - x, 2) + Math.pow(emp.y - y, 2));
                        if (tempMin > d) {
                            tempMin = d;
                        }
                    }

                    if (minDistance < tempMin) {
                        tx = x;
                        ty = y;
                        minDistance = tempMin;
                    }
                }
            }
        }

        if (matrix[tx][ty] != 0) {
            return "There are no more seats.";
        }

        Employee newEmp = new Employee(tx, ty, false);
        employees.put(id, newEmp);
        matrix[tx][ty] = id;
        checkAvailable(tx, ty, -1);

        return id + " gets the seat (" + (tx + 1) + ", " + (ty + 1) + ").";
    }
}
