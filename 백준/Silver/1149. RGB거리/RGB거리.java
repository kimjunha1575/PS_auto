import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    static int length;
    static int[][] dp;
    static int[][] costs;

    public static void main(String args[]) throws IOException {
        getInput();
        System.out.println(bottomUp());
    }
    
    static void getInput() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        length = Integer.parseInt(br.readLine());
        dp = new int[length][3];
        costs = new int[length][3];
        for (int i = 0; i < length; i++) {
            String[] input = br.readLine().split(" ");
            costs[i][0] = Integer.parseInt(input[0]);
            costs[i][1] = Integer.parseInt(input[1]);
            costs[i][2] = Integer.parseInt(input[2]);
        }
        br.close();
    }

    static int topDown() {
        dp[length-1] = costs[length-1];
        int position = length - 2;
        while (position >= 0) {
            dp[position][0] = Math.min(dp[position+1][1], dp[position+1][2]) + costs[position][0];
            dp[position][1] = Math.min(dp[position+1][0], dp[position+1][2]) + costs[position][1];
            dp[position][2] = Math.min(dp[position+1][0], dp[position+1][1]) + costs[position][2];
            position--;
        }
        
        return Math.min(dp[0][0], Math.min(dp[0][1], dp[0][2]));
    }

    static int bottomUp() {
        dp[0] = costs[0];
        int position = 1;
        while (position < length) {
            dp[position][0] = Math.min(dp[position-1][1], dp[position-1][2]) + costs[position][0];
            dp[position][1] = Math.min(dp[position-1][0], dp[position-1][2]) + costs[position][1];
            dp[position][2] = Math.min(dp[position-1][1], dp[position-1][0]) + costs[position][2];
            position++;
        }
        return Math.min(dp[length-1][2], Math.min(dp[length-1][0], dp[length-1][1]));
    }

}
