import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {

	private static int T;
	private static int arrSize;
	private static int[] arr;
	private static PriorityQueue<Integer> highQue, lowQue;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());

		for (int tc = 0; tc < T; tc++) {
			init(br);
			System.out.println((arrSize + 1) / 2);
			int cnt = 0;
			for (int i = 0; i < arrSize; i++) {
				balancedAdd(arr[i]);
				if ((i + 1) % 2 == 1) {
					System.out.printf("%d ", lowQue.peek());
					if (cnt == 9) {
						System.out.println();
						cnt = 0;
					} else cnt++;
				}
			}
			System.out.println();
		}
		br.close();
	}

	public static void balancedAdd(int n) {
		if (lowQue.size() == 0) {
			lowQue.add(n);
			return;
		}
		if (lowQue.peek() > n) {
			highQue.add(n);
			while (highQue.size() > lowQue.size()) {
				lowQue.add(highQue.poll());
			}
		} else {
			lowQue.add(n);
			while (lowQue.size() - highQue.size() > 1) {
				highQue.add(lowQue.poll());
			}
		}
	}

	public static void init(BufferedReader br) throws IOException {
		highQue = new PriorityQueue<>(Collections.reverseOrder());
		lowQue = new PriorityQueue<>();

		arrSize = Integer.parseInt(br.readLine());
		arr = new int[arrSize];
		for (int i = 0; i <= (arrSize - 1) / 10; i++) {
			String[] input = br.readLine().split(" ");
			for (int j = 0; j < input.length; j++) {
				arr[10 * i + j] = Integer.parseInt(input[j]);
			}
		}
	}
}
