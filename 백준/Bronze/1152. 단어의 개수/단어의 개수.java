import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args)  throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int ans = input.length;
        if (ans == 0) {
            System.out.println(0);
            br.close();
            return;
        }
        if (input[input.length-1].equals("")) {
            ans -= 1;
        }
        if (input[0].equals("")) ans -= 1;
        System.out.println(ans);
        br.close();
    }
}