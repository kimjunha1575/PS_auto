import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    static int N, K;

    public static void main(String args[]) throws IOException {
        getInput();
        int result = calculate(N, K);
        System.out.println(result);
    }

    static void getInput() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            String[] input = br.readLine().split(" ");
            N = Integer.parseInt(input[0]);
            K = Integer.parseInt(input[1]);
            br.close();
        }
        catch (Exception e) {
            e.printStackTrace();
            br.close();
        }
    }

    static int calculate(int N, int K) {
        int result = 0;
        int chunk = 1;
        int count = 0;
        while (count < K) {
            chunk = 1;
            while (chunk*2 <= N) {
                chunk *= 2;
            }
            N -= chunk;
            count++;
            
            if (N > 0) {
                continue;
            }
            else break;
        }

        // System.out.printf("count: %d, chunk: %d\n", count, chunk);

        if (N > 0) {
            result = chunk - N;
        }

        return result;
    }

}