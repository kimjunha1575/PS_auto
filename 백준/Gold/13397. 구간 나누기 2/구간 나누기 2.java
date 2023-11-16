import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// https://www.acmicpc.net/problem/13397

public class Main {

	static int[] arr;
	static int arrSize;
	static int groupSize;

	public static void main(String[] args) throws IOException {
		getInput();
		System.out.println(binarySearch());
	}

	public static boolean isPossible(int n) {
		int min = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;
		int cntGroup = 1;
		for (int i = 0; i < arrSize; i++) {
			int tmpMin = min;
			int tmpMax = max;
			if (arr[i] < tmpMin) tmpMin = arr[i];
			if (arr[i] > tmpMax) tmpMax = arr[i];
			if (tmpMax - tmpMin <= n) {
				min = tmpMin;
				max = tmpMax;
			} else {
				cntGroup++;
				min = arr[i];
				max = arr[i];
				if (cntGroup > groupSize) return false;
			}
		}
		return true;
	}

	public static int binarySearch() {
		int left = 0;
		int right = Integer.MAX_VALUE;

		while (left <= right) {
			int mid = (left + right) / 2;
			if (isPossible(mid)) right = mid - 1; else left = mid + 1;
		}
		if (left >= 0) return left; else return right;
	}

	public static void getInput() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input;
		input = br.readLine().split(" ");
		arrSize = Integer.parseInt(input[0]);
		arr = new int[arrSize];
		groupSize = Integer.parseInt(input[1]);
		input = br.readLine().split(" ");
		for (int i = 0; i < arrSize; i++) {
			arr[i] = Integer.parseInt(input[i]);
		}
		br.close();
	}
}
