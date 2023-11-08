import java.util.Arrays;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] meetings = new int[N][2];
        for (int i = 0; i < N; i++) {
            meetings[i][0] = sc.nextInt();
            meetings[i][1] = sc.nextInt();
        }
        Arrays.sort(meetings, (a, b) -> {
            if (a[1] == b[1]) return a[0] - b[0];
            else return a[1] - b[1];
        });
        int cnt = 1;
        int time = meetings[0][1];
        int meeting = 1;
        while (meeting < N) {
            if (meetings[meeting][0] >= time) {
                cnt++;
                time = meetings[meeting][1];
            }
            meeting++;
        }
        System.out.println(cnt);
        sc.close();
    }
}
