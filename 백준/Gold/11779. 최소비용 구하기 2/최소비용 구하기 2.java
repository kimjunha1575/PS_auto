import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {

	private static int cntCity;
	private static int cntBus;
	private static int st, en;
	private static int[][] map;
	private static int[] path;

	public static void main(String[] args) throws IOException {
		init();
		int ans = dijkstra(st, en);
		System.out.println(ans);
		int cnt = 0;
		int idx = en;
		String fullPath = "";
		do {
			fullPath = String.valueOf(idx + " ").concat(fullPath);
			cnt++;
			idx = path[idx];
		} while (idx > 0);
		System.out.println(cnt);
		System.out.println(fullPath);
	}

	public static int dijkstra(int st, int en) {
		PriorityQueue<Bus> pq = new PriorityQueue<>();
		int[] dist = new int[cntCity + 1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		Bus init = new Bus(st, st, 0);
		pq.add(init);
		dist[st] = 0;

		while (!pq.isEmpty()) {
			Bus cur = pq.poll();
			int now = cur.en;
			int cost = cur.cost;
			// System.out.printf("%d: %d\n", now, cost);

			if (now == en) {
				return cost;
			}

			if (dist[en] < cost) continue;

			for (int next = 1; next <= cntCity; next++) {
				if (next == now || map[now][next] == -1) continue;
				int ncost = dist[now] + map[now][next];
				if (dist[next] <= ncost) continue;

				Bus tmp = new Bus(now, next, ncost);
				dist[next] = ncost;
				path[next] = now;
				pq.add(tmp);
			}
		}

		return -1;
	}

	public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input;
		cntCity = Integer.parseInt(br.readLine()); 
		map = new int[cntCity + 1][cntCity + 1];
		for (int[] arr : map) Arrays.fill(arr, -1);
		cntBus = Integer.parseInt(br.readLine()); 
		path = new int[cntCity + 1];
		Arrays.fill(path, -1);
		for (int i = 0; i < cntBus; i++) {
			int st, en, cost;
            input = br.readLine().split(" ");
			st = Integer.parseInt(input[0]); 
			en = Integer.parseInt(input[1]);
			cost = Integer.parseInt(input[2]);
			if (map[st][en] == -1) map[st][en] = cost;
            else if (map[st][en] > cost) map[st][en] = cost;
		}
        input = br.readLine().split(" ");
		st = Integer.parseInt(input[0]);
		en = Integer.parseInt(input[1]);
    	br.close();
	}
}

class Bus implements Comparable<Bus> {

	public int st;
	public int en;
	public int cost;

	public Bus(int st, int de, int co) {
		this.st = st;
		this.en = de;
		this.cost = co;
	}

	public int compareTo(Bus o) {
		return this.cost - o.cost;
	}
}
