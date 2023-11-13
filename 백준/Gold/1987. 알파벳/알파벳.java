import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	static int row, col;
	static char[][] board;
	static int ans;

	static int[] dy = { 0, 1, 0, -1 };
	static int[] dx = { 1, 0, -1, 0 };

	public static void main(String[] args) throws IOException {
		getInput();
        ans = 0;
        Path init = new Path();
        dfs(0, 0, init);
        System.out.println(ans);
	}

	public static void dfs(int y, int x, Path p) {
        if (p.cnt > ans) {
            ans = p.cnt;
        }

		for (int dir = 0; dir < 4; dir++) {
			int ny = y + dy[dir];
			int nx = x + dx[dir];

			if (ny < 0 || nx < 0 || ny >= row || nx >= col) continue;
			int idx = (int) board[ny][nx] - (int) 'A';
			if (p.path[idx]) continue;

			p.path[idx] = true;
			p.cnt += 1;
			dfs(ny, nx, p);
			p.cnt -= 1;
			p.path[idx] = false;
		}
	}

	public static void getInput() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		row = Integer.parseInt(input[0]);
		col = Integer.parseInt(input[1]);
		board = new char[row][col];
		for (int r = 0; r < row; r++) {
			String tmp = br.readLine();
			for (int c = 0; c < col; c++) {
				board[r][c] = tmp.charAt(c);
			}
		}
		br.close();
	}

	static class Path {

		public int cnt;
		public boolean[] path;

		public Path() {
            path = new boolean[26];
			Arrays.fill(path, false);
			this.path[(int) board[0][0] - (int) 'A'] = true;
			this.cnt = 1;
		}
	}
}
