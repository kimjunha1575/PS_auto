
// https://www.acmicpc.net/problem/1991

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tree_size = Integer.parseInt(br.readLine());
        Vertex[] tree = new Vertex[26];
        for (int i = 0; i < tree_size; i++) {
            String[] input = br.readLine().split(" ");
            char data = input[0].charAt(0);
            char left = input[1].charAt(0);
            char right = input[2].charAt(0);
            tree[data - 'A'] = new Vertex(data - 'A', left == '.' ? -1 : left - 'A', right == '.' ? -1 : right - 'A');
        }

        preorder(tree, tree[0].data);
        System.out.println();
        inorder(tree, tree[0]);
        System.out.println();
        postorder(tree, tree[0]);
        br.close();
    }

    public static void preorder(Vertex[] tree, int root) {
        if (root == -1) {
            return;
        }
        System.out.printf("%c", tree[root].data + 'A');
        if (tree[root].left != -1) {
            preorder(tree, tree[root].left);
        }
        if (tree[root].right != -1) {
            preorder(tree, tree[root].right);
        }
    }

    public static void inorder(Vertex[] tree, Vertex root) {
        if (root.left != -1) {
            inorder(tree, tree[root.left]);
        }
        System.out.printf("%c", root.data + 'A');
        if (root.right != -1) {
            inorder(tree, tree[root.right]);
        }
    }

    public static void postorder(Vertex[] tree, Vertex root) {
        if (root.left != -1) {
            postorder(tree, tree[root.left]);
        }
        if (root.right != -1) {
            postorder(tree, tree[root.right]);
        }
        System.out.printf("%c", root.data + 'A');
    }



    static class Vertex {
        public int data;
        public int left;
        public int right;

        public Vertex(int data, int left, int right) {
            this.data = data;
            this.left = left;
            this.right = right;
        }
    }
}

// 완전 객체지향으로 배열 없이 할거면 넣을 때 마다 검색 해야하고
// 배열 넣어서 실행시간 줄이려면 배열로 접근해야하니까 인덱스로 잡는게 더 편하고

