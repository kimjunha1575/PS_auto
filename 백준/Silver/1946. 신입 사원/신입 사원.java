import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test_case;
        test_case = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < test_case; tc++) {
            int candidate_cnt = Integer.parseInt(br.readLine());
            int[] candidates = new int[candidate_cnt];
            for (int i = 0; i < candidate_cnt; i++) {
                String[] input = br.readLine().split(" ");
                int docu_rank = Integer.parseInt(input[0]) - 1;
                candidates[docu_rank] = Integer.parseInt(input[1]) - 1;
            }
            int top_rank = candidates[0];
            int cnt = 1;
            for (int i = 1; i < candidate_cnt; i++) {
                if (candidates[i] < top_rank) {
                    cnt++;
                    top_rank = candidates[i];
                }
            }
            bw.write(String.valueOf(cnt) + '\n');
        }
        bw.flush();
        bw.close();
        br.close();
    }
}