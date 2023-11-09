import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

// https://www.acmicpc.net/problem/1916
public class Main {

	static int cntCity;
	static int cntBus;
	static int[][] map;
	static boolean[] visited;
	static int[] dist;
	static int start_pos, end_pos;

	public static void main(String[] args) throws IOException {
		// init
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input;
		cntCity = Integer.parseInt(br.readLine());
		cntBus = Integer.parseInt(br.readLine());
		map = new int[cntCity + 1][cntCity + 1];
		visited = new boolean[cntCity + 1];
		dist = new int[cntCity + 1];
		Arrays.fill(dist, 0x7FFFFFFF);
		Arrays.fill(visited, false);
		for (int[] arr : map) Arrays.fill(arr, -1);

		// get map input
		for (int i = 0; i < cntBus; i++) {
			int from, to, cost;
			input = br.readLine().split(" ");
			from = Integer.parseInt(input[0]);
			to = Integer.parseInt(input[1]);
			cost = Integer.parseInt(input[2]);
            if (map[from][to] == -1) map[from][to] = cost;
			else if (map[from][to] > cost) map[from][to] = cost;
		}

		// get start&end position
		input = br.readLine().split(" ");
		start_pos = Integer.parseInt(input[0]);
		end_pos = Integer.parseInt(input[1]);

		// calculation (dijkstra)
		dijkstra(start_pos, end_pos);

		// print
		System.out.println(dist[end_pos]);

		// close buffer
		br.close();
	}

	public static void dijkstra(int start, int end) {
		PriorityQueue<Path> pq = new PriorityQueue<>();
		dist[start] = 0;
		Path init = new Path(start, start, dist[start]);
		pq.add(init);

		while (!pq.isEmpty()) {
			Path cur = pq.poll();
			visited[cur.to] = true;
			// System.out.printf("moved %d to %d (cost: %d)\n", cur.from, cur.to, cur.cost);

			if (cur.to == end) break;
			if (dist[cur.to] < cur.cost) continue;

			for (int i = 1; i <= cntCity; i++) {
				if (map[cur.to][i] == -1) continue;
				if (visited[i] == true) continue;
				if (cur.to == i) continue;
				if (cur.cost + map[cur.to][i] >= dist[i]) continue;

				dist[i] = cur.cost + map[cur.to][i];
				Path next = new Path(cur.to, i, dist[i]);
				pq.add(next);
			}
		}
	}
}

class Path implements Comparable<Path> {

	public int from, to, cost;

	public Path(int from, int to, int cost) {
		this.from = from;
		this.to = to;
		this.cost = cost;
	}

	public int compareTo(Path o) {
		return this.cost - o.cost;
	}
}
