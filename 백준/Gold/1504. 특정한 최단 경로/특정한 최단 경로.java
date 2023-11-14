import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.lang.Math;

// https://www.acmicpc.net/problem/1504

public class Main {

	private static int vertices;
	private static int edges;
	private static int[][] map;
	private static int v1, v2;

	public static void main(String[] args) throws IOException {
		init();
		int v1_v2 = dijkstra(v1, v2);
		int st_v1 = dijkstra(1, v1);
		int st_v2 = dijkstra(1, v2);
		int en_v1 = dijkstra(vertices, v1);
		int en_v2 = dijkstra(vertices, v2);
		// Path st_en = dijkstra(1, vertices);

        // System.out.println("=========");
        // System.out.println(v1_v2); // 3
        // System.out.println(st_v1); // 3
        // System.out.println(st_v2); // 5
        // System.out.println(en_v1); // 4
        // System.out.println(en_v2); // 1
        // System.out.println("=========");

        // PriorityQueue<Integer> ans_que = new PriorityQueue<>();
        // ans_que.add(st_v1 + v1_v2 + en_v2);
        // ans_que.add(st_v2 + v1_v2 + en_v1);
        int ans;
        if ( (st_v1 == -1 && st_v2 == -1) || (en_v1 == -1 && en_v2 == -1) || v1_v2 == -1 ) {
            ans = -1;
        }
        else ans = Math.min(st_v1 + v1_v2 + en_v2, st_v2 + v1_v2 + en_v1);

        System.out.println(ans);
	}

	public static int dijkstra(int st, int en) {
		int[] dist = new int[vertices + 1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		Edge init_edge = new Edge(st, st, 0);
		pq.add(init_edge);
		dist[st] = 0;

		while (!pq.isEmpty()) {
			Edge cur = pq.poll();
			int now = cur.to;
			int d = cur.dist;

			if (now == en) return d;

			if (dist[en] < d) continue;

			for (int next = 1; next <= vertices; next++) {
				if (next == now || map[now][next] == -1) continue;
				int nd = d + map[now][next];
				if (dist[next] < nd) continue;

				Edge next_edge = new Edge(now, next, nd);
				dist[next] = nd;
				pq.add(next_edge);
			}
		}

		return -1;
	}

	static class Edge implements Comparable<Edge> {

		public int from;
		public int to;
		public int dist;

		public Edge(int from, int to, int dist) {
			this.from = from;
			this.to = to;
			this.dist = dist;
		}

		public int compareTo(Edge e) {
			return this.dist - e.dist;
		}
	}


	public static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		vertices = Integer.parseInt(input[0]);
		edges = Integer.parseInt(input[1]);
		map = new int[vertices + 1][vertices + 1];
		for (int[] arr : map) Arrays.fill(arr, -1);
		for (int i = 0; i < edges; i++) {
			int from, to, d;
			input = br.readLine().split(" ");
			from = Integer.parseInt(input[0]);
			to = Integer.parseInt(input[1]);
			d = Integer.parseInt(input[2]);
			map[from][to] = d;
			map[to][from] = d;
		}
		input = br.readLine().split(" ");
		v1 = Integer.parseInt(input[0]);
		v2 = Integer.parseInt(input[1]);
		br.close();
	}
}
