import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	static int[] arr;
	static int arr_size;
	static int group_size;

	public static void main(String[] args) throws IOException {
		getInput();
		int ans = binarySearch();
		System.out.println(ans);
	}

	public static boolean isPossible(int n) {
		// System.out.printf("=======n: %d=======\n", n);
		int min = Integer.MAX_VALUE;
		int max = 0;
		int group_cnt = 1;
		for (int i = 0; i < arr_size; i++) {
			int min_tmp = min;
			int max_tmp = max;
			if (arr[i] < min_tmp) min_tmp = arr[i];
			if (arr[i] > max_tmp) max_tmp = arr[i];
			// System.out.printf("i: %d\nmin: %d\nmax: %d\n", i, min_tmp, max_tmp);
			if (max_tmp - min_tmp <= n) {
				min = min_tmp;
				max = max_tmp;
			} else {
				// System.out.println("new group");
				group_cnt++;
				min = arr[i];
				max = arr[i];
				if (group_cnt > group_size) return false;
			}
		}
		// System.out.println("true");
		return true;
	}

	public static int binarySearch() {
		int left = 0;
		int right = Integer.MAX_VALUE;

		while (left <= right) {
			int mid = (left + right) / 2;
			if (isPossible(mid)) right = mid - 1; else left = mid + 1;
		}
		// System.out.printf("left: %d\nright: %d\n", left, right);
		if (left >= 0) return left; else return right;
	}

	public static void getInput() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input;
		input = br.readLine().split(" ");
		arr_size = Integer.parseInt(input[0]);
		arr = new int[arr_size];
		group_size = Integer.parseInt(input[1]);
		input = br.readLine().split(" ");
		for (int i = 0; i < arr_size; i++) {
			arr[i] = Integer.parseInt(input[i]);
		}
		br.close();
	}
}
