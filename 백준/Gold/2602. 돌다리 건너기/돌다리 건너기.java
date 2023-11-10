import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	static String magic_scroll;
	static String angel_bridge;
	static String demon_bridge;
	static String[] map;
	static int[][] dp_d;
	static int[][] dp_a;

	public static void main(String[] args) throws IOException {
		getInput();
		if (magic_scroll.length() > angel_bridge.length()) {
			System.out.println(0);
		} else {
			solve();
			System.out.println(dp_a[0][0] + dp_d[0][0]);
		}
	}

	public static void solve() {
		int row = magic_scroll.length();
		int col = angel_bridge.length();
		int idx = 0;

		// angel first
		// set map
		map = new String[col];
		for (int i = 0; i < row; i++) {
			if (i % 2 == 0) map[i] = angel_bridge; else map[i] = demon_bridge;
		}
		// set dp_a's bottom row
		int cnt = 0;
		for (int i = col - 1; i >= 0; i--) {
			if (map[row - 1].charAt(i) == magic_scroll.charAt(row - 1)) {
				if (cnt == 0) idx = i;
				cnt++;
			}
			dp_a[row - 1][i] = cnt;
		}
		// bottom up
		for (int r = row - 2; r >= 0; r--) {
			cnt = 0;
			int tmp = idx;
			for (int c = tmp - 1; c >= 0; c--) {
				if (map[r].charAt(c) == magic_scroll.charAt(r)) {
					if (cnt == 0) idx = c;
					cnt = dp_a[r + 1][c + 1] + dp_a[r][c + 1];
				}
				dp_a[r][c] = cnt;
			}
		}

		idx = 0;
		// demon first
		// set map
		for (int i = 0; i < row; i++) {
			if (i % 2 == 1) map[i] = angel_bridge; else map[i] = demon_bridge;
		}
		// set dp_a's bottom row
		cnt = 0;
		for (int i = col - 1; i >= 0; i--) {
			if (map[row - 1].charAt(i) == magic_scroll.charAt(row - 1)) {
				if (cnt == 0) idx = i;
				cnt++;
			}
			dp_d[row - 1][i] = cnt;
		}
		// bottom up
		for (int r = row - 2; r >= 0; r--) {
			cnt = 0;
			int tmp = idx;
			for (int c = tmp - 1; c >= 0; c--) {
				if (map[r].charAt(c) == magic_scroll.charAt(r)) {
					if (cnt == 0) idx = c;
					cnt = dp_d[r + 1][c + 1] + dp_d[r][c + 1];
				}
				dp_d[r][c] = cnt;
			}
		}
	}

	public static void getInput() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		magic_scroll = br.readLine();
		angel_bridge = br.readLine();
		demon_bridge = br.readLine();
		int row = magic_scroll.length();
		int col = angel_bridge.length();
		dp_a = new int[row][col];
		for (int[] arr : dp_a) Arrays.fill(arr, 0);
		dp_d = new int[row][col];
		for (int[] arr : dp_d) Arrays.fill(arr, 0);
		br.close();
	}
}
