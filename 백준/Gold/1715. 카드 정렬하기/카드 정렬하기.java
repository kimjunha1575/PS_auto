import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    static int N;
    static PriorityQueue<Integer> deck_sizes;

    public static void main(String[] args) throws IOException {
        init();
        System.out.println(solution());
    }

    public static int solution() {
        int ans = 0;
        
        while (deck_sizes.size() > 1) {
            int tmp = deck_sizes.poll() + deck_sizes.poll();
            ans += tmp;
            deck_sizes.add(tmp);
        }
        return ans;
    }

    public static void init() throws IOException {
        deck_sizes = new PriorityQueue<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            int deck = Integer.parseInt(br.readLine());
            deck_sizes.add(deck);
        }
        br.close();
    }
}
