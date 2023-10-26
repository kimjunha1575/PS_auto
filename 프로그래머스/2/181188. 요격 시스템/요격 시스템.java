import java.util.Comparator;
import java.util.Arrays;

class Solution {
    public int solution(int[][] targets) {
        if (targets.length == 1) {
            return 1;
        }
        int ans = 1;
        Arrays.sort(targets, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }
        });
        int left = 0;
        int right = 1;
        while (right <= targets.length - 1) {
            if (targets[right][0] < targets[left][1]) {
                right++;
                continue;
            }
            else {
                ans++;
                left = right;
                right++;
                continue;
            }
        }
        return ans;
    }
}