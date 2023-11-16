import java.io.*;
import java.util.*;

public class Main {

	private static final int[] dr = { -1, 0, 1, 1, 1, 0, -1, -1 };
	private static final int[] dc = { 1, 1, 1, 0, -1, -1, -1, 0 };
	private static ArrayList<Integer> heights;
	private static char[][] map;
	private static int[][] height;
	private static int officeHeight;
	private static int cntHouse;
	private static int startR, startC;
	private static int min, max;
	private static int N;

	public static void main(String[] args) throws IOException {
		getInput();
		min = Math.min(officeHeight, min);
		max = Math.max(officeHeight, max);
		Collections.sort(heights);
		System.out.println(twoPointer());
	}

	public static int bfs(int low, int high) {
        if (low > officeHeight || high < officeHeight) return 0;
		int ret = 0;
		Queue<int[]> que = new LinkedList<>();
		boolean[][] visited = new boolean[N][N];
		for (boolean[] r : visited) Arrays.fill(r, false);

		que.add(new int[] { startR, startC });
		visited[startR][startC] = true;

		while (!que.isEmpty()) {
			int[] cur = que.poll();

			for (int dir = 0; dir < 8; dir++) {
				int nr = cur[0] + dr[dir];
				int nc = cur[1] + dc[dir];

				if (nr < 0 || nr >= N || nc < 0 || nc >= N) {
					continue;
				}
				if (visited[nr][nc]) {
					continue;
				}
				if (height[nr][nc] < low || height[nr][nc] > high) {
					continue;
				}
				que.add(new int[] { nr, nc });
				visited[nr][nc] = true;
                if (map[nr][nc] == 'K') {
                    ret++;
                }
                if (ret >= cntHouse) return ret;
			}
		}

		return ret;
	}

	public static int twoPointer() {
		int leftPtr = 0;
		int rightPtr = 0;
        int limit = heights.indexOf(officeHeight);
		int ans = Integer.MAX_VALUE;

		while (leftPtr <= rightPtr && rightPtr < heights.size()) {
			int low = heights.get(leftPtr);
			int high = heights.get(rightPtr);

			if (bfs(low, high) >= cntHouse) {
				ans = Math.min(ans, high - low);
				leftPtr++;
			} else {
				rightPtr++;
			}
		}
		return ans;
	}

	public static void getInput() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new char[N][N];
		height = new int[N][N];
		heights = new ArrayList<>();

		min = Integer.MAX_VALUE;
		max = Integer.MIN_VALUE;

		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for (int j = 0; j < N; j++) {
				map[i][j] = line.charAt(j);
				if (map[i][j] == 'P') {
					startR = i;
					startC = j;
				}
				if (map[i][j] == 'K') {
					cntHouse++;
				}
			}
		}

		for (int i = 0; i < N; i++) {
			String[] line = br.readLine().split(" ");
			for (int j = 0; j < N; j++) {
				height[i][j] = Integer.parseInt(line[j]);
				if (map[i][j] == 'P') {
					officeHeight = height[i][j];
				} else if (map[i][j] == 'K') {
					min = Math.min(min, height[i][j]);
					max = Math.max(max, height[i][j]);
				}
				if (heights.contains(height[i][j])) {
					continue;
				}
				heights.add(height[i][j]);
			}
		}
		br.close();
	}
}
