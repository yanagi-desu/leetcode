import java.util.*;
class main {
    public static void main(String [] args){
        Solution solution = new Solution();
        solution.solution();
        System.out.println("Hi");
    }
}

class Solution{
    public int solution(Node root){
        if(root == null) return 0;
        Queue<Node> q = new LinkedList<>();
        q.offer(root);
        int level = 0;
        while(!q.isEmpty()){
            int len = q.size();
            for(int i=0;i<len;i++){
                Node temp = q.poll();
                for(Node each:temp.children){
                    q.offer(each);
                }
            }
            level++;
        }
        return level;
    }
}

class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};